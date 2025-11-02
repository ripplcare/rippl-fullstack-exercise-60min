# Contributing Guidelines

Thank you for your interest in completing the Rippl Full-Stack 60-Minute Exercise!

Please read these quick notes before you begin.

---

## 🚀 How to Submit

1. **Fork this repository** to your own GitHub account.  
2. Complete the challenge in your forked copy.  
3. When ready, **open a Pull Request** back to the `main` branch of the original repo.  
   - Use the PR title format:  
     ```
     [Your Name] - Full Stack Exercise Submission
     ```
   - You don’t need a lengthy write-up - a few sentences describing what you focused on or trade-offs you made is plenty.

---

## 🧭 Guidelines

- Keep your work within the provided structure (`problem/api`, `problem/web`).
- All API (`pytest`) and UI (`vitest`) tests should pass.
- Feel free to refactor or improve structure if it clarifies your approach.
- No external dependencies or libraries should be added unless absolutely necessary.
- Avoid committing generated files (node_modules, .pyc, etc).

---

## 🧹 Housekeeping

Before submitting, please:

- Run `python3 -m pytest -q` (API)
- Run `npm test` (Web)
- Verify that `npm run dev` and the API (`flask run`) both start without errors.

---

## 💬 Questions

If anything in the instructions is unclear, note your assumptions in the PR description.  
We’re not evaluating setup troubleshooting - we’re evaluating how you think, code, and communicate.

---

© 2025 Ripplcare, Inc. All rights reserved.
