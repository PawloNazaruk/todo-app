
# Configuration of database and it's connection

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database file Path
SQLITE_DATABASE_URL = "sqlite:///./notes.sqlite"

engine = create_engine(
    SQLITE_DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# TODO - Until connection is maintained the db can be accessed??
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
