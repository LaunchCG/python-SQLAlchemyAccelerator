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

def check_no_duplicates(db, table_name):
    query = text(f"SELECT {TABLES[table_name]['columns']['all']} FROM {table_name}")
    df = pd.read_sql(query, db)
    duplicates = df[df.duplicated()]
    assert duplicates.empty, f"Duplicated data found in '{table_name}'"

def check_no_nulls_in_required_columns(db, table_name, required_columns):
    query = text(f"SELECT {TABLES[table_name]['columns']['all']} FROM {table_name}")
    df = pd.read_sql(query, db)
    for column in required_columns:
        nulls = df[column].isnull().sum()
        assert nulls == 0, f"There are null values in non-nullable column '{column}' in '{table_name}'"

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

def test_data_consistency(db):
    for check in CONSISTENCY_CHECKS:
        if check["type"] == "no_duplicates":
            check_no_duplicates(db, check["table"])
        elif check["type"] == "no_nulls":
            check_no_nulls_in_required_columns(db, check["table"], check["required_columns"])

