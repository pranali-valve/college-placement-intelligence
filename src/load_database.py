import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os


# Load environment variables
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
engine = create_engine(DATABASE_URL)


# CSV file
csv_path = "data/raw/students_raw.csv"


# Load CSV
df = pd.read_csv(csv_path)

print("CSV loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# Insert students data
student_columns = [
    "student_id",
    "branch",
    "cgpa",
    "tenth_percentage",
    "twelfth_percentage",
    "backlogs",
    "internships",
    "projects",
    "certifications",
    "technical_skills",
    "aptitude_score",
    "communication_score",
    "attendance",
    "placement_year"
]

students_df = df[student_columns]

students_df.to_sql(
    "students",
    engine,
    if_exists="append",
    index=False
)

print("Students data inserted successfully!")


# Insert placements data
placement_columns = [
    "student_id",
    "placed",
    "company",
    "package_lpa"
]

placements_df = df[placement_columns]

placements_df.to_sql(
    "placements",
    engine,
    if_exists="append",
    index=False
)

print("Placements data inserted successfully!")


# Verify database
with engine.connect() as connection:

    students_count = pd.read_sql(
        "SELECT COUNT(*) AS count FROM students",
        connection
    ).iloc[0]["count"]

    placements_count = pd.read_sql(
        "SELECT COUNT(*) AS count FROM placements",
        connection
    ).iloc[0]["count"]


print("\n========== DATABASE VERIFICATION ==========")
print("Students records:", students_count)
print("Placement records:", placements_count)
print("===========================================")

print("\nDatabase loading completed successfully!")