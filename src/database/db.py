from sqlalchemy import create_engine
import os

# Load database credentials from environment variables (recommended for security)
DATABASE_USER = os.getenv('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'root')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'pytest_workshop')

# Construct the database URI
DATABASE_URI = f'mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URI, pool_pre_ping=True)

# Optional: ORM session integration
# from sqlalchemy.orm import sessionmaker
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_connection():
    """
    Establish and return a database connection.

    Returns:
        connection: A SQLAlchemy connection object.
    """
    try:
        connection = engine.connect()
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise