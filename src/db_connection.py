"""
db_connection.py
----------------
Reusable MySQL connection helper using SQLAlchemy + .env credentials.
"""

import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

def get_engine():
    """Create and return a SQLAlchemy engine for MySQL."""
    username = os.getenv("DB_USERNAME", "root")
    password = os.getenv("DB_PASSWORD", "")
    host     = os.getenv("DB_HOST", "localhost")
    port     = os.getenv("DB_PORT", "3306")
    database = os.getenv("DB_NAME", "customer_behavior")

    connection_url = (
        f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    )
    engine = create_engine(connection_url, echo=False)
    return engine


def test_connection():
    """Quick connectivity check — prints OK or the error."""
    try:
        engine = get_engine()
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ MySQL connection successful!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")


if __name__ == "__main__":
    test_connection()