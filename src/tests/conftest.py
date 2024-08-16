import pytest
from database.db import get_connection

@pytest.fixture(scope="module")
def db():
    # need to create a connection
    connection = get_connection()
    try:
        yield connection
    finally:
        connection.close()
