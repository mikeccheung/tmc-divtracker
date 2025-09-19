"""Dividend record model."""

from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String

from .base import Base


class Dividend(Base):
    """Individual dividend event tied to a transaction or standalone."""

    __tablename__ = "dividends"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id", ondelete="SET NULL"), nullable=True)
    ticker = Column(String, nullable=False, index=True)
    ex_date = Column(Date, nullable=True)
    pay_date = Column(Date, nullable=True)
    amount = Column(Numeric(18, 6), nullable=False)
    currency = Column(String, nullable=False, default="USD")
