from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os


# Load environment variables from .env
load_dotenv() 


# Database configuration
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# Encode password safely
encoded_password = quote_plus(DB_PASSWORD)


# PostgreSQL connection URL
DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{encoded_password}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}
)


# Test connection
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("PostgreSQL connection successful!")
    except Exception as e:
        print("Database connection failed!")
        print(e)