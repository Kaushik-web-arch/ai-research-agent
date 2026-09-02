"""Offline tests for private local caching and report exports."""

import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from models import CachedReport
from storage import ReportStore


class ReportStoreTests(unittest.TestCase):
    def test_cache_round_trip_and_markdown_export(self):
        with tempfile.TemporaryDirectory() as directory:
            store = ReportStore(root=directory, cache_hours=24)
            key = store.cache_key("Research AI", "Standard", "Student", "Balanced", "test-model")
            cached = CachedReport(
                cache_key=key,
                query="Research AI",
                mode="Standard",
                audience="Student",
                report_style="Balanced",
                model="test-model",
                report="# Report\n\nEvidence.",
                search_count=3,
                source_count=4,
                created_at=datetime.now(timezone.utc),
            )

            store.save(cached)
            loaded = store.load(key)
            export = store.export_markdown(cached.query, cached.report)

            self.assertIsNotNone(loaded)
            self.assertEqual(loaded.report, cached.report)
            self.assertTrue(Path(export).exists())
            self.assertEqual(Path(export).read_text(encoding="utf-8"), cached.report)


if __name__ == "__main__":
    unittest.main()
