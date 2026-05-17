# API Test Automation Project

Automation framework built with Python, Requests and Pytest.

## Features
- CRUD API testing (GET, POST, PUT, PATCH, DELETE)
- GET single user
- Positive and negative API scenarios
- Parametrized API tests
- Reusable API client
- Validation of status codes and response body
- HTML reports

## Tech Stack
- Python
- Requests
- Pytest

## Run Tests

```bash
pip install -r requirements.txt
pytest
```

Generate HTML report:

```bash
pytest --html=report.html
```

## Project Structure

tests/ - API test cases  
utils/ - reusable API client  
conftest.py - fixtures