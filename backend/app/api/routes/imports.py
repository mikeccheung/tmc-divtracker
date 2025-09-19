"""Import endpoints for CSV ingestion."""

from datetime import datetime
from typing import Any, Dict

from fastapi import APIRouter, File, HTTPException, UploadFile

from ...schemas.imports import ImportCreateResponse, ImportPreviewResponse, ParsedTransaction

router = APIRouter(prefix="/imports", tags=["imports"])


@router.post("", response_model=ImportCreateResponse)
async def create_import(file: UploadFile = File(...)) -> ImportCreateResponse:
    """Receive an uploaded CSV file and create an import job."""

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported in this prototype.")

    # Placeholder job identifier; replace with persistence in Sprint 1.
    job_id = 1

    return ImportCreateResponse(import_id=job_id, status="pending")


@router.get("/{import_id}/preview", response_model=ImportPreviewResponse)
async def get_import_preview(import_id: int) -> ImportPreviewResponse:
    """Return a parsed preview for an uploaded file."""

    if import_id < 1:
        raise HTTPException(status_code=404, detail="Import job not found.")

    sample_rows = [
        ParsedTransaction(
            source_row=1,
            detected_type="DIVIDEND",
            ticker="AAPL",
            trade_date="2024-03-01",
            quantity=None,
            price=None,
            amount=24.56,
            notes="Sample data",
        ),
        ParsedTransaction(
            source_row=2,
            detected_type="BUY",
            ticker="MSFT",
            trade_date="2024-02-15",
            quantity=10,
            price=320.12,
            amount=-3201.2,
            notes="Sample data",
        ),
    ]

    return ImportPreviewResponse(
        import_id=import_id,
        status="ready",
        rows=sample_rows,
        detected_broker="robinhood",
        generated_at=datetime.utcnow(),
    )


@router.post("/{import_id}/confirm")
async def confirm_import(import_id: int) -> Dict[str, Any]:
    """Persist parsed transactions after user confirmation."""

    if import_id < 1:
        raise HTTPException(status_code=404, detail="Import job not found.")

    return {"import_id": import_id, "status": "confirmed"}
