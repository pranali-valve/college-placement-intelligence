import pandas as pd


# Load dataset
df = pd.read_csv("data/raw/students_raw.csv")


print("========== DATA VALIDATION ==========\n")


# ---------------------------------------------------
# 1. CGPA validation
# ---------------------------------------------------

invalid_cgpa = df[
    (df["cgpa"] < 0) |
    (df["cgpa"] > 10)
]

print("Invalid CGPA records:", len(invalid_cgpa))


# ---------------------------------------------------
# 2. 10th percentage validation
# ---------------------------------------------------

invalid_tenth = df[
    (df["tenth_percentage"] < 0) |
    (df["tenth_percentage"] > 100)
]

print("Invalid 10th percentage records:", len(invalid_tenth))


# ---------------------------------------------------
# 3. 12th percentage validation
# ---------------------------------------------------

invalid_twelfth = df[
    (df["twelfth_percentage"] < 0) |
    (df["twelfth_percentage"] > 100)
]

print("Invalid 12th percentage records:", len(invalid_twelfth))


# ---------------------------------------------------
# 4. Backlog validation
# ---------------------------------------------------

invalid_backlogs = df[
    df["backlogs"] < 0
]

print("Invalid backlog records:", len(invalid_backlogs))


# ---------------------------------------------------
# 5. Attendance validation
# ---------------------------------------------------

invalid_attendance = df[
    (df["attendance"] < 0) |
    (df["attendance"] > 100)
]

print("Invalid attendance records:", len(invalid_attendance))


# ---------------------------------------------------
# 6. Aptitude score validation
# ---------------------------------------------------

invalid_aptitude = df[
    (df["aptitude_score"] < 0) |
    (df["aptitude_score"] > 100)
]

print("Invalid aptitude records:", len(invalid_aptitude))


# ---------------------------------------------------
# 7. Communication score validation
# ---------------------------------------------------

invalid_communication = df[
    (df["communication_score"] < 0) |
    (df["communication_score"] > 100)
]

print(
    "Invalid communication score records:",
    len(invalid_communication)
)


# ---------------------------------------------------
# 8. Placement target validation
# ---------------------------------------------------

invalid_placed = df[
    ~df["placed"].isin([0, 1])
]

print("Invalid placement records:", len(invalid_placed))


# ---------------------------------------------------
# 9. Placement consistency
# ---------------------------------------------------

invalid_company = df[
    ((df["placed"] == 1) & (df["company"] == "Not Placed")) |
    ((df["placed"] == 0) & (df["company"] != "Not Placed"))
]

print(
    "Invalid company/placement combinations:",
    len(invalid_company)
)


# ---------------------------------------------------
# 10. Package consistency
# ---------------------------------------------------

invalid_package = df[
    ((df["placed"] == 0) & (df["package_lpa"] != 0)) |
    ((df["placed"] == 1) & (df["package_lpa"] <= 0))
]

print(
    "Invalid package/placement combinations:",
    len(invalid_package)
)


# ---------------------------------------------------
# Final result
# ---------------------------------------------------

total_errors = (
    len(invalid_cgpa)
    + len(invalid_tenth)
    + len(invalid_twelfth)
    + len(invalid_backlogs)
    + len(invalid_attendance)
    + len(invalid_aptitude)
    + len(invalid_communication)
    + len(invalid_placed)
    + len(invalid_company)
    + len(invalid_package)
)


print("\n========== VALIDATION RESULT ==========")

if total_errors == 0:
    print("Data validation successful!")
    print("No invalid records found.")
else:
    print("Invalid records found:", total_errors)