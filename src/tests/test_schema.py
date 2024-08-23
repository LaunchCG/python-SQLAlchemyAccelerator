from sqlalchemy import inspect

# Constants for expected tables, columns, and their data types
TABLES = {
    'consultant': {
        'consultant_discipline': 'VARCHAR',
        'consultant_location': 'VARCHAR',
        'consultant_name': 'VARCHAR',
        'consultant_title': 'VARCHAR',
        'idconsultant': 'INTEGER'
    },
    'discipline': {
        'discipline_name': 'VARCHAR',
        'studio_name': 'VARCHAR',
        'iddiscipline': 'INTEGER'
    },
    'studio': {
        'idstudio': 'INTEGER',
        'studio_name': 'VARCHAR'
    }
    # New tables and columns can be added here
}

# Function to validate tables, columns, and their data types
def test_validate_tables_and_columns(db):
    """
    Validate that the expected tables, columns, and data types exist in the database schema.

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
        actual_columns = {col['name']: col['type'].__class__.__name__.upper() for col in columns}

        # Check if the expected columns are a subset of the actual columns
        for column_name, expected_type in expected_columns.items():
            assert column_name in actual_columns, f"Column '{column_name}' does not exist in table '{table_name}'"
            actual_type = actual_columns[column_name]
            assert actual_type == expected_type, f"Column '{column_name}' in table '{table_name}' has type '{actual_type}', expected '{expected_type}'"

        # Check for any missing columns
        missing_columns = set(expected_columns.keys()) - set(actual_columns.keys())
        assert not missing_columns, f"Schema validation failed for table '{table_name}': missing columns {missing_columns}"