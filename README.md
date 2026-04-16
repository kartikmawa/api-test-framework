# API Test Framework (Python + pytest)

## 📌 Overview

This project demonstrates a simple API automation framework using Python and pytest.
It validates API responses including status codes, structure, and data correctness.

## 🚀 Features

* API testing using requests
* pytest framework with fixtures
* Parametrized test execution
* Reusable validation functions
* Positive and negative test coverage

## 🧪 Test Coverage

* Status code validation
* Response structure validation
* Data type validation
* Field value validation

## 📂 Project Structure

```
api-tests/
│
├── tests/
│     └── test_posts.py
│
├── utils/
│     ├── api_client.py
│     └── validators.py
```

## ⚙️ Setup & Run

### Install dependencies

```
pip install -r requirements.txt
```

### Run tests

```
pytest
```

## 📌 Sample Output

* Tests run for multiple post IDs
* Validates both success (200) and failure (404) scenarios

## 💡 Learning Outcome

This project demonstrates how to build a scalable and maintainable API test framework using pytest.
