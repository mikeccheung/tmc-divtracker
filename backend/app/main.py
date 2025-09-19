"""FastAPI application entry point."""

from datetime import datetime
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.routes import auth, imports
from .core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.project_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=settings.api_v1_prefix)
app.include_router(imports.router, prefix=settings.api_v1_prefix)


@app.get("/health", tags=["health"])
def healthcheck() -> Dict[str, Any]:
    """Simple health check endpoint."""

    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}
