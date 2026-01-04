# SauceDemo Playwright Automation

This project demonstrates how to automate login testing for [saucedemo.com](https://www.saucedemo.com/) using both Playwright for TypeScript/JavaScript and Playwright for Python.

## Prerequisites
- Node.js (for TypeScript/JavaScript tests)
- Python 3 (preferably installed via Homebrew, for Python tests)
- [uv](https://github.com/astral-sh/uv) (for Python dependency management)

---

## 1. Running Playwright Tests (TypeScript/JavaScript)

### Setup
1. Install dependencies:
   ```sh
   npm install
   ```
2. Install Playwright browsers:
   ```sh
   npx playwright install
   ```

### Run the Test
- To run the login test in **headless** mode (no UI):
  ```sh
  npx playwright test login.spec.ts
  ```
- To run the test in **headed** mode (show browser UI):
  ```sh
  npx playwright test login.spec.ts --headed
  ```

### Playwright Test Runner UI (TypeScript/JavaScript only)
- Playwright for TypeScript/JavaScript provides an interactive UI for running and debugging tests.
- To launch the Playwright Test Runner UI:
  ```sh
  npx playwright test --ui
  ```
- This opens a graphical interface where you can select, run, debug, and inspect tests interactively.
- **Note:** The `--ui` flag is not available in the Python version of Playwright.

---

## 2. Running Playwright Tests (Python)

### Setup
1. Create and activate the virtual environment (if not already):
   ```sh
   uv venv --python $(which python3) .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   uv pip install -r requirements.txt
   playwright install
   ```

### Run the Test
- To run the login test in **headless** mode (no UI):
  ```sh
  pytest test_login_saucedemo.py
  ```
- To run the test in **headed** mode (show browser UI):
  Edit `test_login_saucedemo.py` and change `headless=True` to `headless=False` in the line:
  ```python
  browser = p.chromium.launch(headless=True)
  # Change to:
  browser = p.chromium.launch(headless=False)
  ```
  Then run:
  ```sh
  pytest test_login_saucedemo.py
  ```

---

## Project Structure
- `login.spec.ts` — Playwright test in TypeScript
- `test_login_saucedemo.py` — Playwright test in Python
- `requirements.txt` — Python dependencies
- `package.json` — Node.js dependencies

---

## Notes
- Both test scripts perform login to saucedemo.com using the credentials:
  - Username: `standard_user`
  - Password: `secret_sauce`
- Make sure to install all dependencies and browsers before running tests.

