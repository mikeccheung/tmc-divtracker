"""Schemas for import endpoints."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ImportCreateResponse(BaseModel):
    """Response returned after a file upload is initiated."""

    import_id: int
    status: str


class ParsedTransaction(BaseModel):
    """Representation of a parsed transaction row in preview."""

    source_row: int
    detected_type: str
    ticker: Optional[str]
    trade_date: Optional[str]
    quantity: Optional[float]
    price: Optional[float]
    amount: Optional[float]
    notes: Optional[str]


class ImportPreviewResponse(BaseModel):
    """Preview payload returned to the client."""

    import_id: int
    status: str
    rows: List[ParsedTransaction]
    detected_broker: Optional[str]
    generated_at: datetime
