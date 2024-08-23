import time
from sqlalchemy import text

# Constants for configuration
QUERY_LIMIT = 1000
MAX_EXECUTION_TIME = 2  # seconds
TABLE_NAME = "consultant"
ID_COLUMN = "idconsultant"

# Function to test query performance
def test_query_performance(db, table_name=TABLE_NAME, id_column=ID_COLUMN):
    """
    Test the performance of a query by measuring its execution time.

    Args:
    db: Database connection object.
    table_name (str): Name of the table to query.
    id_column (str): Name of the ID column in the table.
    """
    query = text(f"SELECT * FROM {table_name} WHERE {id_column} < :query_limit")
    
    start_time = time.time()
    result = db.execute(query, {"query_limit": QUERY_LIMIT}).fetchall()
    end_time = time.time()
    
    execution_time = end_time - start_time
    assert execution_time < MAX_EXECUTION_TIME, f"Query took too long: {execution_time:.2f} seconds"