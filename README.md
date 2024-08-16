# python-dbtesting
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
git clone https://github.com/mdelhoyo-launch/python-dbtesting.git
cd your-repo-name
pip install -r requirements.txt
```


Make sure to have the following packages in your requirements.txt:
```bash
SQLAlchemy
mysqlclient
pytest
pandas
```

## Project Structure
The project is organized as follows:
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
└── requirements.txt         # List of dependencies
```

## Database Configuration
The database connection is configured in the **database/db.py** file. Update the **DATABASE_URL** with your MySQL credentials as follows.

## Database connection configuration
```python
DATABASE_URL = 'mysql://username:password@localhost/mydatabase' #example

engine = create_engine(DATABASE_URL)
```


## Running the Tests
To run the tests, simply execute:
```bash
pytest
```