from sqlalchemy import create_engine

DATABASE_URI = 'mysql://root:root@localhost/pytest_workshop'

engine = create_engine(DATABASE_URI)

# in case we integrate ORM
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_connection():
    return engine.connect()