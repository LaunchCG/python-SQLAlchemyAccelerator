import pandas as pd
from sqlalchemy import text

# Constants for tables and columns
TABLES = {
    "consultant": {
        "columns": {
            "required": ['consultant_name', 'idconsultant'],
            "all": "*"
        }
    }
}

# Function to check for duplicate records in a table
def check_no_duplicates(db, table_name):
    query = text(f"SELECT {TABLES[table_name]['columns']['all']} FROM {table_name}")
    df = pd.read_sql(query, db)
    duplicates = df[df.duplicated()]
    assert duplicates.empty, f"Duplicated data found in '{table_name}': {duplicates}"

# Function to check for null values in required columns of a table
def check_no_nulls_in_required_columns(db, table_name, required_columns):
    query = text(f"SELECT {TABLES[table_name]['columns']['all']} FROM {table_name}")
    df = pd.read_sql(query, db)
    for column in required_columns:
        nulls = df[column].isnull().sum()
        assert nulls == 0, f"There are {nulls} null values in non-nullable column '{column}' in '{table_name}'"

# List of consistency checks to perform
CONSISTENCY_CHECKS = [
    {
        "type": "no_duplicates",
        "table": "consultant"
    },
    {
        "type": "no_nulls",
        "table": "consultant",
        "required_columns": TABLES["consultant"]["columns"]["required"]
    }
]

# Test function to run all consistency checks
def test_data_consistency(db):
    for check in CONSISTENCY_CHECKS:
        if check["type"] == "no_duplicates":
            check_no_duplicates(db, check["table"])
        elif check["type"] == "no_nulls":
            check_no_nulls_in_required_columns(db, check["table"], check["required_columns"])