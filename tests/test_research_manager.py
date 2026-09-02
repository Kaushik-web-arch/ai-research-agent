"""Offline tests: these tests never call Gemini or the web."""

import asyncio
import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from config import Settings, load_settings
from models import ResearchFinding, SearchItem, Source
from research_manager import ResearchManager


class FakeCompletions:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return next(self.responses)


def fake_gemini_client(responses):
    completions = FakeCompletions(responses)
    client = SimpleNamespace(chat=SimpleNamespace(completions=completions))
    return client, completions


class FakeSearch:
    def __init__(self, results, extracts=None):
        self.results = results
        self.extracts = extracts or {}
        self.text_calls = []
        self.extract_calls = []

    def text(self, query, **kwargs):
        self.text_calls.append((query, kwargs))
        return self.results

    def extract(self, url, **kwargs):
        self.extract_calls.append((url, kwargs))
        value = self.extracts.get(url)
        if isinstance(value, Exception):
            raise value
        return {"url": url, "content": value or ""}


class ResearchManagerTests(unittest.TestCase):
    def setUp(self):
        settings = Settings(
            api_key="test-key-not-used",
            model="gemini-3.5-flash-lite",
            search_count=3,
            report_word_target=1000,
            cache_hours=24,
        )
        self.manager = ResearchManager(settings=settings, client=SimpleNamespace())

    def test_google_key_is_preferred(self):
        with patch.dict(
            os.environ,
            {"GOOGLE_API_KEY": "twin-key", "GEMINI_API_KEY": "other-key"},
        ):
            self.assertEqual(load_settings().api_key, "twin-key")

    def test_clean_search_results_deduplicates_and_removes_fragments(self):
        results = [
            {"title": "Example", "href": "https://example.com/a#one", "body": "First"},
            {"title": "Duplicate", "href": "https://example.com/a#two", "body": "Second"},
            {"title": "Other", "href": "https://example.com/b", "body": "Third"},
        ]

        cleaned = self.manager._clean_search_results(results)

        self.assertEqual(
            [source.url for source, _ in cleaned],
            ["https://example.com/a", "https://example.com/b"],
        )

    def test_clean_search_results_rejects_unsafe_and_private_urls(self):
        results = [
            {"title": "Unsafe", "href": "javascript:alert(1)"},
            {"title": "Localhost", "href": "http://127.0.0.1/private"},
            {"title": "Metadata", "href": "http://169.254.169.254/latest"},
            {"title": "Valid", "href": "https://example.com/page"},
        ]

        cleaned = self.manager._clean_search_results(results)

        self.assertEqual([source.url for source, _ in cleaned], ["https://example.com/page"])

    def test_format_evidence_includes_notes_and_links(self):
        finding = ResearchFinding(
            query="sample query",
            reason="sample reason",
            notes="sample findings",
            sources=[Source(title="Primary source", url="https://example.com")],
        )

        evidence = self.manager._format_evidence([finding])

        self.assertIn("sample findings", evidence)
        self.assertIn("[Primary source](https://example.com)", evidence)

    def test_source_lines_are_unique(self):
        source = Source(title="Example", url="https://example.com")
        findings = [
            ResearchFinding(query="one", reason="one", notes="one", sources=[source]),
            ResearchFinding(query="two", reason="two", notes="two", sources=[source]),
        ]

        lines = self.manager._source_lines(findings)

        self.assertEqual(lines, ["- [Example](https://example.com)"])

    def test_plan_searches_uses_openai_compatible_chat_completion(self):
        response = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(
                        content='```json\n{"searches": ['
                        '{"query": "first query", "reason": "first reason"},'
                        '{"query": "second query", "reason": "second reason"},'
                        '{"query": "third query", "reason": "third reason"}'
                        ']}\n```'
                    )
                )
            ]
        )
        client, completions = fake_gemini_client([response])
        self.manager._client = client

        plan = self.manager.plan_searches("sample topic")

        self.assertEqual(len(plan.searches), 3)
        self.assertEqual(completions.calls[0]["model"], "gemini-3.5-flash-lite")
        self.assertEqual(completions.calls[0]["messages"][0]["role"], "system")

    def test_research_item_uses_keyless_search_and_page_extracts(self):
        search = FakeSearch(
            results=[
                {
                    "title": "Primary evidence",
                    "href": "https://example.com/research",
                    "body": "A useful current snippet.",
                },
                {
                    "title": "Second source",
                    "href": "https://example.org/analysis",
                    "body": "A second perspective.",
                },
            ],
            extracts={"https://example.com/research": "Detailed page evidence."},
        )
        self.manager._search_client = search
        item = SearchItem(query="focused query", reason="useful evidence")

        finding = self.manager.research_item("original question", item, max_results=5, extract_limit=1)

        self.assertEqual(len(finding.sources), 2)
        self.assertIn("Detailed page evidence.", finding.notes)
        self.assertEqual(search.text_calls[0][1]["max_results"], 5)
        self.assertEqual(len(search.extract_calls), 1)

    def test_research_item_falls_back_to_snippet_when_extract_fails(self):
        search = FakeSearch(
            results=[
                {"title": "Evidence", "href": "https://example.com", "body": "Useful snippet."}
            ],
            extracts={"https://example.com": RuntimeError("blocked")},
        )
        self.manager._search_client = search

        finding = self.manager.research_item(
            "question", SearchItem(query="query", reason="reason"), extract_limit=1
        )

        self.assertIn("Useful snippet.", finding.notes)
        self.assertEqual(finding.sources[0].url, "https://example.com")

    def test_write_report_adds_sources_when_model_omits_them(self):
        response = SimpleNamespace(
            choices=[
                SimpleNamespace(message=SimpleNamespace(content="# Report\n\nUseful answer."))
            ]
        )
        client, completions = fake_gemini_client([response])
        self.manager._client = client
        finding = ResearchFinding(
            query="query",
            reason="reason",
            notes="notes",
            sources=[Source(title="Evidence", url="https://example.com/evidence")],
        )

        report = self.manager.write_report("question", [finding])

        self.assertIn("## Sources", report)
        self.assertIn("[Evidence](https://example.com/evidence)", report)
        self.assertNotIn("tools", completions.calls[0])

    def test_json_extractor_rejects_non_json_output(self):
        with self.assertRaisesRegex(RuntimeError, "invalid_search_plan"):
            self.manager._extract_json_object("no structured plan returned")

    def test_timeout_error_is_explained_to_the_user(self):
        update = self.manager._friendly_error(RuntimeError("planning_timeout"))

        self.assertIn("70 seconds", update.markdown)
        self.assertEqual(update.status, "Run stopped safely")

    def test_provider_timeout_is_converted_to_stage_timeout(self):
        def fail_with_timeout():
            raise RuntimeError("The request timed out")

        with self.assertRaisesRegex(RuntimeError, "planning_timeout"):
            asyncio.run(
                self.manager._run_with_timeout(
                    fail_with_timeout, 1, "planning_timeout"
                )
            )


if __name__ == "__main__":
    unittest.main()
