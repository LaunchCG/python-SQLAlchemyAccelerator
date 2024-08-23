import pytest
from database.db import get_connection

@pytest.fixture(scope="module")
def db():
    """
    Fixture to create a database connection for the duration of the test module.
    """
    connection = None
    try:
        connection = get_connection()
        yield connection
    except Exception as e:
        pytest.fail(f"Failed to establish database connection: {e}")
    finally:
        if connection:
            connection.close()

def pytest_configure(config):
    """
    Configure pytest metadata for HTML reports.
    """
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = "SQLAlchemy Accelerator"
        config._metadata['Database'] = "MySQL"
        config._metadata['Module'] = "Database validation"

@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    """
    Customize the title of the HTML report.
    """
    report.title = "Database Schema Validation Report"