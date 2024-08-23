from sqlalchemy import inspect

# Constants for expected tables and columns
TABLES = {
    'consultant': [
        'consultant_discipline', 
        'consultant_location', 
        'consultant_name', 
        'consultant_title', 
        'idconsultant'
    ],
    'discipline': [
        'discipline_name', 
        'studio_name', 
        'iddiscipline'
    ],
    'studio': [
        'idstudio', 
        'studio_name'
    ]
    # New tables and columns can be added here
}

# Function to validate tables and columns
def test_validate_tables_and_columns(db):
    """
    Validate that the expected tables and columns exist in the database schema.

    Args:
    db: Database connection object.
    """
    inspector = inspect(db)
    tables = inspector.get_table_names()

    for table_name, expected_columns in TABLES.items():
        # Check if the table exists
        assert table_name in tables, f"Table '{table_name}' does not exist in the selected schema"

        # Get the actual columns of the table
        columns = inspector.get_columns(table_name)
        actual_columns = {col['name'] for col in columns}

        # Check if the expected columns are a subset of the actual columns
        missing_columns = set(expected_columns) - actual_columns
        assert not missing_columns, f"Schema validation failed for table '{table_name}': missing columns {missing_columns}"