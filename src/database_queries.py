# =========================================================
# DATABASE QUERIES
# =========================================================

import pandas as pd
from src.database_connection import engine


# ---------------------------------------------------------
# 1. TOTAL STUDENTS
# ---------------------------------------------------------

def get_total_students():

    query = """
        SELECT COUNT(*) AS total_students
        FROM students;
    """

    df = pd.read_sql(query, engine)

    return int(df.iloc[0]["total_students"])


# ---------------------------------------------------------
# 2. TOTAL PLACED STUDENTS
# ---------------------------------------------------------

def get_placed_students():

    query = """
        SELECT COUNT(*) AS placed_students
        FROM placements
        WHERE placed = 1;
    """

    df = pd.read_sql(query, engine)

    return int(df.iloc[0]["placed_students"])


# ---------------------------------------------------------
# 3. AVERAGE PACKAGE
# ---------------------------------------------------------

def get_average_package():

    query = """
        SELECT AVG(package_lpa) AS average_package
        FROM placements
        WHERE placed = 1;
    """

    df = pd.read_sql(query, engine)

    return round(float(df.iloc[0]["average_package"]), 2)


# ---------------------------------------------------------
# 4. HIGHEST PACKAGE
# ---------------------------------------------------------

def get_highest_package():

    query = """
        SELECT MAX(package_lpa) AS highest_package
        FROM placements
        WHERE placed = 1;
    """

    df = pd.read_sql(query, engine)

    return round(float(df.iloc[0]["highest_package"]), 2)


# ---------------------------------------------------------
# 5. BRANCH-WISE PLACEMENT
# ---------------------------------------------------------

def get_branch_placement():

    query = """
        SELECT
            s.branch,
            COUNT(*) AS total_students,
            SUM(
                CASE WHEN p.placed = 1 THEN 1 ELSE 0 END
            ) AS placed_students,
            ROUND(
                100.0 *
                SUM(CASE WHEN p.placed = 1 THEN 1 ELSE 0 END)
                / COUNT(*),
                2
            ) AS placement_rate
        FROM students s
        JOIN placements p
            ON s.student_id = p.student_id
        GROUP BY s.branch
        ORDER BY placement_rate DESC;
    """

    return pd.read_sql(query, engine)


# ---------------------------------------------------------
# 6. YEAR-WISE PLACEMENT
# ---------------------------------------------------------

def get_year_placement():

    query = """
        SELECT
            s.placement_year,
            COUNT(*) AS total_students,
            SUM(
                CASE WHEN p.placed = 1 THEN 1 ELSE 0 END
            ) AS placed_students,
            ROUND(
                100.0 *
                SUM(CASE WHEN p.placed = 1 THEN 1 ELSE 0 END)
                / COUNT(*),
                2
            ) AS placement_rate
        FROM students s
        JOIN placements p
            ON s.student_id = p.student_id
        GROUP BY s.placement_year
        ORDER BY s.placement_year;
    """

    return pd.read_sql(query, engine)


# ---------------------------------------------------------
# TEST DATABASE QUERIES
# ---------------------------------------------------------

if __name__ == "__main__":

    print("======================================")
    print("DATABASE QUERY TEST")
    print("======================================")

    print("Total Students:",
          get_total_students())

    print("Placed Students:",
          get_placed_students())

    print("Average Package:",
          get_average_package(), "LPA")

    print("Highest Package:",
          get_highest_package(), "LPA")

    print()
    print("Branch-wise Placement:")
    print(get_branch_placement())

    print()
    print("Year-wise Placement:")
    print(get_year_placement())

    print()
    print("Database queries working successfully!")