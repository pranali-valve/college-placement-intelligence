# =========================================================
# FETCH COMPLETE DATA FROM POSTGRESQL
# =========================================================

import pandas as pd
from src.database_connection import engine


def get_all_student_data():

    query = """
        SELECT
            s.student_id,
            s.branch,
            s.cgpa,
            s.tenth_percentage,
            s.twelfth_percentage,
            s.backlogs,
            s.internships,
            s.projects,
            s.certifications,
            s.technical_skills,
            s.aptitude_score,
            s.communication_score,
            s.attendance,
            p.placed,
            p.company,
            p.package_lpa,
            s.placement_year

        FROM students s

        JOIN placements p
            ON s.student_id = p.student_id

        ORDER BY s.student_id;
    """

    df = pd.read_sql(query, engine)

    return df


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    print("======================================")
    print("POSTGRESQL DATA FETCH TEST")
    print("======================================")

    df = get_all_student_data()

    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print()
    print("Columns:")
    print(df.columns.tolist())

    print()
    print("First 5 records:")
    print(df.head())

    print()
    print("Data fetched successfully!")