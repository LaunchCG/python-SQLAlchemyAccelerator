# SQLAlchemy Accelerator
Python automated scripts for database testing

This project demonstrates how to use SQLAlchemy to interact with a MySQL database and how to write automated tests using pytest. It includes examples for schema validation, query performance analysis and data consistency checks.

Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Database Configuration](#database-configuration)
- [Database connection configuration](#database-connection-configuration)
- [Running the Tests](#running-the-tests)

## Installation
To get started, clone the repository and install the necessary dependencies:
```bash
git clone https://github.com/LaunchCG/python-SQLAlchemyAccelerator.git
cd your-repo-name
pip install -r requirements.txt
```


Make sure to have the following packages in your requirements.txt:
```bash
SQLAlchemy
mysqlclient
pytest
pandas
pytest-html
```

## Project Structure
The project is organized as shown above:
```bash
src/
│
├── database/
│   ├── db.py                # Database configuration and connection
│
├── tests/
│   ├── conftest.py          # Pytest configuration (fixtures)
│   ├── test_schema.py       # Tests for schema validation
│   ├── test_performance.py  # Tests for query performance
│   ├── test_consistency.py  # Tests for data consistency
│
├── .env                     # Environment variables for sensitive information.
├── pytest.ini               # Configuration file for pytest
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
```

## Database Configuration
The database connection is configured in the **src/database/db.py** file. Update the environment variables in the **.env** file with your MySQL credentials as shown above.

## Database connection configuration
```python
DATABASE_USER = os.getenv('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'root')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'pytest_workshop')
```

## Running the Tests
To run the tests, simply execute:
```bash
pytest
```