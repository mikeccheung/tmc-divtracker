-- Core database schema for Dividend Tracker MVP

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE portfolios (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    currency TEXT NOT NULL DEFAULT 'USD'
);

CREATE TABLE imports (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    filename TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    uploaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    source TEXT
);

CREATE TYPE transaction_type AS ENUM ('BUY', 'SELL', 'DIVIDEND', 'DRIP');

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    portfolio_id INTEGER NOT NULL REFERENCES portfolios(id) ON DELETE CASCADE,
    type transaction_type NOT NULL,
    ticker TEXT NOT NULL,
    trade_date DATE NOT NULL,
    quantity NUMERIC(18, 6),
    price NUMERIC(18, 6),
    fees NUMERIC(18, 6),
    amount NUMERIC(18, 6),
    raw_import_id INTEGER REFERENCES imports(id),
    canonicalized_flag BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE dividends (
    id SERIAL PRIMARY KEY,
    transaction_id INTEGER REFERENCES transactions(id) ON DELETE SET NULL,
    ticker TEXT NOT NULL,
    ex_date DATE,
    pay_date DATE,
    amount NUMERIC(18, 6) NOT NULL,
    currency TEXT NOT NULL DEFAULT 'USD'
);

CREATE TABLE subscriptions (
    user_id INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    plan TEXT NOT NULL,
    stripe_customer_id TEXT,
    active_until TIMESTAMPTZ
);

CREATE INDEX idx_transactions_portfolio_date ON transactions (portfolio_id, trade_date);
CREATE INDEX idx_dividends_ticker_pay_date ON dividends (ticker, pay_date);
