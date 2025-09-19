# Repository Structure

```
.
├── README.md
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── requirements.txt
├── db/
│   └── schema.sql
├── docs/
│   ├── repo_structure.md
│   └── stripe_cognito_checklist.md
└── frontend/
    ├── index.html
    ├── package.json
    ├── src/
    │   ├── components/
    │   └── pages/
    ├── tailwind.config.js
    └── vite.config.ts
```

Each directory contains focused responsibilities:

- `backend/app` – FastAPI application, routers, domain models, and parsing services.
- `frontend` – React + TypeScript client bootstrapped with Vite and Tailwind CSS.
- `db` – Database schema artifacts and migrations.
- `docs` – Developer documentation, deployment checklists, and architectural notes.
