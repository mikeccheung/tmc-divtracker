"""Transaction database model."""

from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from .base import Base

TRANSACTION_TYPES = ("BUY", "SELL", "DIVIDEND", "DRIP")


class Transaction(Base):
    """Canonical representation of a brokerage transaction."""

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id", ondelete="CASCADE"), nullable=False, index=True)
    type = Column(String, nullable=False)
    ticker = Column(String, nullable=False, index=True)
    trade_date = Column(Date, nullable=False)
    quantity = Column(Float, nullable=True)
    price = Column(Numeric(18, 6), nullable=True)
    fees = Column(Numeric(18, 6), nullable=True)
    amount = Column(Numeric(18, 6), nullable=True)
    raw_import_id = Column(Integer, ForeignKey("imports.id"), nullable=True)
    canonicalized_flag = Column(Integer, nullable=False, default=0)

    portfolio = relationship("Portfolio", backref="transactions")
    import_job = relationship("ImportJob")
