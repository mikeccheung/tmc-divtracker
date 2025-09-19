"""Import job metadata model."""

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from .base import Base


class ImportJob(Base):
    """Represents an uploaded brokerage statement awaiting processing."""

    __tablename__ = "imports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    filename = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    source = Column(String, nullable=True)
