"""Portfolio database model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Portfolio(Base):
    """A collection of holdings belonging to a user."""

    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String, nullable=False)
    currency = Column(String, nullable=False, default="USD")

    owner = relationship("User", backref="portfolios")
