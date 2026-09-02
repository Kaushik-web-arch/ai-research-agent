"""Structured data models used by the research workflow."""

from datetime import datetime

from pydantic import BaseModel, Field


class SearchItem(BaseModel):
    query: str = Field(min_length=3, description="A focused web search query")
    reason: str = Field(min_length=3, description="Why this search is useful")


class SearchPlan(BaseModel):
    searches: list[SearchItem] = Field(
        min_length=2,
        max_length=5,
        description="Focused searches that together answer the user's question",
    )


class Source(BaseModel):
    title: str
    url: str


class ResearchFinding(BaseModel):
    query: str
    reason: str
    notes: str
    sources: list[Source] = Field(default_factory=list)


class CachedReport(BaseModel):
    cache_key: str
    query: str
    mode: str
    audience: str
    report_style: str
    model: str
    report: str
    search_count: int
    source_count: int
    created_at: datetime


class ResearchUpdate(BaseModel):
    markdown: str
    status: str
    report_path: str | None = None
    is_final: bool = False
    from_cache: bool = False
