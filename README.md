# Dividend Tracker MVP

This repository contains the initial scaffolding for the dividend-tracking MVP described in the product brief. It ships with:

- ✅ **Backend skeleton** – FastAPI project with authentication and import endpoints ready for expansion.
- ✅ **Frontend skeleton** – React + TypeScript + Tailwind UI shell featuring the Import Review mock.
- ✅ **Database schema** – PostgreSQL SQL script capturing core tables and relationships.
- ✅ **CSV parsing utilities** – Sample fuzzy column mapper and Robinhood parser prototype.
- ✅ **Integration checklists** – Cognito + Stripe setup notes to accelerate onboarding.

## Repository Layout

See [`docs/repo_structure.md`](docs/repo_structure.md) for a visual map of the directories and responsibilities.

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- (Optional) Docker for running local dependencies

## Getting Started – Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Copy and edit environment variables
cp ../.env.example .env  # (create the file if it does not exist yet)
uvicorn app.main:app --reload
```

Environment variables expected by the backend:

| Variable | Description |
| --- | --- |
| `DATABASE_URL` | SQLAlchemy-compatible Postgres URL (`postgresql+psycopg2://...`). |
| `S3_BUCKET_NAME` | Target S3 bucket for raw CSV uploads. |
| `AWS_REGION` | AWS region for S3/Cognito resources (default `us-east-1`). |

## Getting Started – Frontend

```bash
cd frontend
npm install
npm run dev
```

The Vite dev server runs on [http://localhost:3000](http://localhost:3000) and consumes the FastAPI backend at `http://localhost:8000` by default.

## Database Schema

Apply the core schema to a local PostgreSQL instance:

```bash
psql $DATABASE_URL -f db/schema.sql
```

## Sample CSV Parser

A prototype parser lives at [`backend/app/services/parsing/fuzzy_mapper.py`](backend/app/services/parsing/fuzzy_mapper.py). It demonstrates:

- Fuzzy header matching via `rapidfuzz`.
- Normalization of Robinhood-style CSVs into canonical columns.
- Simple activity classification heuristics.

Usage example:

```python
from app.services.parsing.fuzzy_mapper import parse_robinhood_csv

normalized = parse_robinhood_csv("~/Downloads/robinhood_activity.csv")
print(normalized.head())
```

## Import Review UI Mock

The React wireframe for the Import Review workflow lives at [`frontend/src/components/ImportReview.tsx`](frontend/src/components/ImportReview.tsx). It provides:

- Responsive layout with Tailwind classes.
- Selection toggles for including/excluding parsed rows.
- Summary card for quick validation.

## Next Steps

1. Implement persistent storage for import jobs and transactions (Sprint 1).
2. Connect Cognito hosted UI for Google SSO, swapping the stubbed `/auth/sso/google` endpoint with JWT validation.
3. Wire the React Import Review component to the real preview endpoint once parsing pipeline returns actual data.
4. Expand parsing heuristics for additional broker formats as sample CSVs become available.

Refer to [`docs/stripe_cognito_checklist.md`](docs/stripe_cognito_checklist.md) when integrating billing and authentication providers.
