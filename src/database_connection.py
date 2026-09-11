from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv
import streamlit as st
import os


# Load environment variables from .env
load_dotenv()


# Database configuration
DB_USER = st.secrets["DB_USER"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
DB_HOST = st.secrets["DB_HOST"]
DB_PORT = st.secrets["DB_PORT"]
DB_NAME = st.secrets["DB_NAME"]


# Check data types (does NOT show password)
print("DB_USER:", type(DB_USER))
print("DB_PASSWORD:", type(DB_PASSWORD))
print("DB_HOST:", type(DB_HOST))
print("DB_PORT:", type(DB_PORT))
print("DB_NAME:", type(DB_NAME))


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