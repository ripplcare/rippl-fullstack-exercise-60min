# Rippl Full-Stack 60-Minute Exercise

Starter for a 60-minute full-stack coding challenge.
You will implement both backend and frontend functionality until all provided tests pass.

---

## Overview

Rippl reimagines mental health care for seniors with dementia and their caregivers.
This challenge mirrors a simplified version of Rippl's scheduling workflow.

You will implement a small API and UI that together let a caregiver:

- Create appointments
- View a list of appointments
- Handle overlapping, idempotent, and time-based scheduling rules

---

## What You Will Implement

### Backend (problem/api/app.py)

Implement:

- POST /v1/appointments
- GET /v1/appointments

Your code should:

- Validate request bodies and timestamps
- Enforce:
  - Duration between 15 and 120 minutes
  - Business hours: 08:00 - 18:00 America/Los_Angeles
- Reject overlapping appointments for the same caregiver (409 APPT_OVERLAP)
- Support an Idempotency-Key header:
  - Same key + same body -> return the same 201 response
  - Same key + different body -> return 409 IDEMPOTENCY_KEY_MISMATCH
- Return JSON in this format:

```json
{
  "id": 1,
  "caregiverId": "c1",
  "patientId": "p1",
  "start": "2025-03-10T16:00:00Z",
  "end": "2025-03-10T16:30:00Z"
}
```

---

### Frontend (problem/web/src/App.tsx)

Implement:

- Loading appointments for a caregiver (GET /v1/appointments)
- Sorting the list by start time
- Creating appointments via the form (POST /v1/appointments)
- Basic optimistic UI update (add immediately, rollback on error)
- Simple error display when validation fails

Tests expect:

- A Load button that populates the list
- A list element with data-testid="list"
- Items displayed in ascending order of start

---

## Tests

You must pass:

- Backend tests: problem/api/tests/test_api.py
- Frontend tests: problem/web/src/__tests__/App.test.tsx

### Run backend tests

```bash
cd problem/api
python3 -m pip install -r requirements.txt
python3 -m pytest -q
```

### Run frontend tests

```bash
cd ../web
npm install
npm test
```

Both suites must pass for full credit.

---

## Run the App Locally

1. Start the API

```bash
cd problem/api
python -m flask --app app.py run
```

The API will listen on http://127.0.0.1:5000

2. Start the frontend

```bash
cd ../web
npm run dev
```

Open http://localhost:5173

---

## Time Box

You have 60 minutes total.
If you do not finish, push what you have and include short notes on what you would do next.

---

## Submission

1. Fork this repo or clone it into your own private repo.
2. Implement your solution until all tests pass.
3. Push your changes and open a pull request with your name in the title:

```
[Your Name] - Full Stack Exercise Submission
```

4. Optional: include a short summary of your approach or trade-offs.

---

## Tips

- Use the tests as your spec - they describe the required behavior precisely.
- Focus on correctness, clarity, and edge-case handling.
- Keep external dependencies to a minimum.
- Use logging sparingly (no PHI).

---

## Tech Stack

- Backend: Python (Flask, SQLAlchemy, Pytest)
- Frontend: React, TypeScript, Vite, Vitest
- Database: SQLite (in-memory)
- Environment: Runs entirely locally

---

(c) 2025 Ripplcare. All rights reserved.
