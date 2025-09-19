"""Authentication endpoints."""

from typing import Any, Dict

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/sso/google")
def google_sso_callback(token: str) -> Dict[str, Any]:
    """Stub endpoint for handling Google SSO tokens."""

    # TODO: Integrate with AWS Cognito or Clerk verification.
    if not token:
        raise HTTPException(status_code=400, detail="Invalid SSO token provided.")

    return {
        "status": "success",
        "message": "Token accepted for downstream processing.",
        "token_preview": token[:10],
    }
