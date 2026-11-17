# API
## Tech Stack
* Python 3.10+
* Pytest
* Requests
* Pydantic (for models validation)
* Allure (for reporting)

## Project Structure
* `src/main/api/` - Framework source code
  * `configs/` - Configs
  * `foundation/` - Requesters and Endpoints
  * `models/` - Pydantic schemas
  * `steps/` - Business logic steps
  * `tests/` - Test cases

## Setup
1. Clone the repo
2. Create virtual environment:
   `python -m venv .venv`
3. Activate it and install dependencies:
   `pip install -r requirements.txt`

## Running Tests
Run all tests:
`pytest src/main/api/tests/`

## Allure Report Generation
Run tests with allure listener:
`pytest src/main/api/tests/ --alluredir=allure-results`

Serve the report:
`allure serve allure-results`