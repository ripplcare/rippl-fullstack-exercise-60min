# Rippl Full-Stack 60-Minute Exercise

**A hands-on coding challenge for Rippl engineering candidates. Build, test, and extend a simple scheduling app using Flask and React.**

---

## 🧭 Quick Start

### 1. Run the API tests
```bash
cd problem/api
python3 -m pip install -r requirements.txt
python3 -m pytest -q

All tests (problem/api/tests/test_api.py) should pass before you move on.

2. Start the API (optional)

If you want to try the UI against a running backend:

python -m flask --app app.py run

The API will start at http://127.0.0.1:5000.

3. Run the UI

cd ../web
npm install
npm run dev

Then open http://localhost:5173 in your browser.

4. Run UI tests

npm test

This runs the minimal UI test suite (problem/web/src/__tests__/App.test.tsx).

⸻

🧩 What You’ll Build
	•	A small Flask API (problem/api/app.py) that creates and lists appointments.
	•	A React UI (problem/web/src/App.tsx) that fetches and displays them.

You’ll work primarily in those two files.

The API tests are your specification - all of them must pass.

⸻

📅 Example Data

When using the UI, the form requires four fields:

Field	Example value	Notes
patientId	p1	Any short string identifier.
start	2025-03-10T16:00:00Z	ISO 8601 UTC time — must be between 08:00 and 18:00 Pacific Time.
end	2025-03-10T16:30:00Z	Same format, 15–120 minutes after start.
notes	check-in call	Optional.

Example valid submission:

patientId: p44
start: 2025-03-11T18:00:00Z
end: 2025-03-11T19:00:00Z
notes: session prep

The list will update immediately when a new appointment is created.

⸻

🕐 Time Box

You have 60 minutes total.

If you run out of time, submit what you have and describe next steps or trade-offs in your PR.

⸻

✅ Submission
	1.	Fork this repo or create a feature branch.
	2.	Push your solution.
	3.	Open a pull request to main.

That’s it - no screenshots or write-ups required.

⸻

💡 Tips
	•	Run tests often - they’re fast and will guide your progress.
	•	Log only non-PHI information (caregiverId, patientId, timestamps).
	•	Keep your code readable - clarity > cleverness.
	•	Everything runs locally (no external services required).

⸻

🧱 Tech Stack
	•	Backend: Python 3.11, Flask, SQLAlchemy, Pytest
	•	Frontend: React, TypeScript, Vite, Vitest
	•	CI/CD: GitHub Actions (Python & Node jobs)

⸻

© 2025 Ripplcare, Inc. All rights reserved.
