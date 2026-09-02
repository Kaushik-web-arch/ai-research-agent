"""Application configuration and quota-conscious research profiles."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv(override=True)


def _bounded_int(name: str, default: int, minimum: int, maximum: int) -> int:
    """Read an integer setting and keep it inside a safe range."""
    raw_value = os.getenv(name, str(default)).strip()
    try:
        value = int(raw_value)
    except ValueError:
        return default
    return max(minimum, min(value, maximum))


@dataclass(frozen=True)
class Settings:
    api_key: str | None
    model: str
    search_count: int
    report_word_target: int
    cache_hours: int


@dataclass(frozen=True)
class ResearchProfile:
    name: str
    search_count: int
    results_per_search: int
    pages_to_extract: int
    report_word_target: int

    @property
    def estimated_gemini_requests(self) -> int:
        """One planning call plus one report-writing call."""
        return 2


RESEARCH_PROFILES = {
    "Quick": ResearchProfile(
        "Quick", search_count=2, results_per_search=4, pages_to_extract=1, report_word_target=650
    ),
    "Standard": ResearchProfile(
        "Standard", search_count=3, results_per_search=5, pages_to_extract=2, report_word_target=1000
    ),
    "Deep": ResearchProfile(
        "Deep", search_count=4, results_per_search=6, pages_to_extract=2, report_word_target=1400
    ),
}


def get_research_profile(name: str) -> ResearchProfile:
    """Return a known profile, defaulting safely to Standard."""
    return RESEARCH_PROFILES.get(name, RESEARCH_PROFILES["Standard"])


def load_settings() -> Settings:
    """Load settings without ever printing or exposing the API key."""
    # Prefer the conventional Google AI Studio environment variable.
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    return Settings(
        api_key=api_key.strip() if api_key else None,
        model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite").strip(),
        search_count=_bounded_int("HOW_MANY_SEARCHES", 3, 2, 5),
        report_word_target=_bounded_int("REPORT_WORD_TARGET", 1000, 600, 1500),
        cache_hours=_bounded_int("CACHE_HOURS", 24, 1, 168),
    )
