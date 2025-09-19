"""Fuzzy column mapping utilities for brokerage CSV imports."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable

import pandas as pd
from rapidfuzz import fuzz, process


@dataclass
class ColumnMatch:
    """Represents the mapping between canonical and source columns."""

    canonical_name: str
    source_name: str
    score: float


CANONICAL_COLUMNS: Dict[str, Iterable[str]] = {
    "date": ("date", "trade date", "activity date", "processed at"),
    "description": ("description", "activity", "type"),
    "amount": ("amount", "value", "net amount", "total"),
    "quantity": ("quantity", "shares", "units"),
    "price": ("price", "share price", "per share"),
    "fees": ("fees", "commission", "charges"),
    "ticker": ("symbol", "ticker", "security"),
}


def _normalize_header(name: str) -> str:
    return name.strip().lower()


def match_columns(headers: Iterable[str], *, threshold: int = 70) -> Dict[str, ColumnMatch]:
    """Match CSV headers to canonical names using fuzzy matching."""

    normalized_headers = [_normalize_header(h) for h in headers]
    matches: Dict[str, ColumnMatch] = {}

    for canonical, _ in CANONICAL_COLUMNS.items():
        best = process.extractOne(
            canonical,
            normalized_headers,
            scorer=fuzz.token_set_ratio,
        )
        if best and best[1] >= threshold:
            source_header = headers[normalized_headers.index(best[0])]
            matches[canonical] = ColumnMatch(canonical, source_header, best[1])

    return matches


def parse_robinhood_csv(path: str) -> pd.DataFrame:
    """Parse a Robinhood activity CSV into a normalized DataFrame."""

    df = pd.read_csv(path)
    mappings = match_columns(df.columns)

    required = {"date", "description", "amount"}
    missing = required - mappings.keys()
    if missing:
        raise ValueError(f"Missing expected columns: {', '.join(sorted(missing))}")

    normalized = pd.DataFrame()
    normalized["trade_date"] = pd.to_datetime(df[mappings["date"].source_name])
    normalized["description"] = df[mappings["description"].source_name].astype(str)
    normalized["amount"] = (
        df[mappings["amount"].source_name]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    if "quantity" in mappings:
        normalized["quantity"] = (
            df[mappings["quantity"].source_name].astype(str).str.replace(",", "", regex=False)
        )
    else:
        normalized["quantity"] = None

    if "price" in mappings:
        normalized["price"] = (
            df[mappings["price"].source_name].astype(str).str.replace(",", "", regex=False)
        )
    else:
        normalized["price"] = None

    if "ticker" in mappings:
        normalized["ticker"] = df[mappings["ticker"].source_name].astype(str).str.upper()
    else:
        normalized["ticker"] = None

    normalized["detected_type"] = normalized["description"].str.upper().map(
        {
            "DIVIDEND": "DIVIDEND",
            "DIVIDENDS": "DIVIDEND",
            "REINVESTMENT": "DRIP",
            "BUY": "BUY",
            "SELL": "SELL",
        }
    ).fillna("UNKNOWN")

    return normalized
