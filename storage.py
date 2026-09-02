"""Private local cache and Markdown export helpers."""

from __future__ import annotations

import hashlib
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

from models import CachedReport


class ReportStore:
    def __init__(self, root: str | Path = ".research_data", cache_hours: int = 24):
        self.root = Path(root)
        self.cache_dir = self.root / "cache"
        self.export_dir = self.root / "exports"
        self.cache_hours = cache_hours

    @staticmethod
    def cache_key(query: str, mode: str, audience: str, report_style: str, model: str) -> str:
        payload = "|".join(
            [query.casefold().strip(), mode.casefold(), audience.casefold(), report_style.casefold(), model]
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def load(self, cache_key: str) -> CachedReport | None:
        cache_file = self.cache_dir / f"{cache_key}.json"
        if not cache_file.exists():
            return None
        try:
            cached = CachedReport.model_validate_json(cache_file.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None

        created_at = cached.created_at
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=timezone.utc)
        if datetime.now(timezone.utc) - created_at > timedelta(hours=self.cache_hours):
            return None
        return cached

    def save(self, cached: CachedReport) -> None:
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        destination = self.cache_dir / f"{cached.cache_key}.json"
        temporary = destination.with_suffix(".tmp")
        temporary.write_text(cached.model_dump_json(indent=2), encoding="utf-8")
        temporary.replace(destination)

    def export_markdown(self, query: str, report: str) -> Path:
        self.export_dir.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^a-z0-9]+", "-", query.casefold()).strip("-")[:55] or "research-report"
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        path = self.export_dir / f"{slug}-{timestamp}.md"
        path.write_text(report, encoding="utf-8")
        return path.resolve()
