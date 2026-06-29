"""
===========================================================
Bharat Sahayak AI
Database Initializer
===========================================================
"""

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import engine
from app.db.base import Base

from app.models.user import User
from app.models.scheme import Scheme

def create_database_tables() -> None:
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)


def test_database_connection() -> bool:
    """
    Verify that the application can connect
    to the configured database.
    """

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return True

    except SQLAlchemyError as error:

        print(f"Database Connection Error : {error}")

        return False


def initialize_database() -> None:
    """
    Initialize database during application startup.
    """

    print("=" * 60)
    print("Initializing Bharat Sahayak AI Database")
    print("=" * 60)

    if test_database_connection():

        print("Database Connection Successful")

        create_database_tables()

        print("Database Initialized Successfully")

    else:

        print("Database Initialization Failed")