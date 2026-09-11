import pandas as pd
import numpy as np

# For reproducible results
np.random.seed(42)

# Number of students
num_students = 1250

# Student IDs
student_ids = [f"S{str(i).zfill(4)}" for i in range(1, num_students + 1)]

# Branches
branches = np.random.choice(
    ["Computer", "IT", "Electronics", "Mechanical", "Civil"],
    size=num_students
)

# Academic and student information
cgpa = np.round(np.random.uniform(5.0, 10.0, num_students), 2)

tenth_percentage = np.round(
    np.random.uniform(55, 98, num_students), 2
)

twelfth_percentage = np.round(
    np.random.uniform(50, 95, num_students), 2
)

backlogs = np.random.choice(
    [0, 1, 2, 3, 4],
    size=num_students,
    p=[0.65, 0.18, 0.09, 0.05, 0.03]
)

internships = np.random.choice(
    [0, 1, 2, 3],
    size=num_students,
    p=[0.35, 0.35, 0.20, 0.10]
)

projects = np.random.choice(
    [0, 1, 2, 3, 4, 5],
    size=num_students,
    p=[0.05, 0.15, 0.25, 0.25, 0.20, 0.10]
)

certifications = np.random.choice(
    [0, 1, 2, 3, 4, 5],
    size=num_students,
    p=[0.20, 0.25, 0.25, 0.15, 0.10, 0.05]
)

technical_skills = np.random.choice(
    [1, 2, 3, 4, 5, 6, 7, 8],
    size=num_students
)

aptitude_score = np.round(
    np.random.uniform(40, 100, num_students), 2
)

communication_score = np.round(
    np.random.uniform(40, 100, num_students), 2
)

attendance = np.round(
    np.random.uniform(60, 100, num_students), 2
)


# ---------------------------------------------------
# Generate placement probability score
# ---------------------------------------------------

score = (
    0.30 * cgpa
    + 0.10 * (tenth_percentage / 10)
    + 0.08 * (twelfth_percentage / 10)
    - 0.15 * backlogs
    + 0.12 * internships
    + 0.10 * projects
    + 0.05 * certifications
    + 0.08 * technical_skills
    + 0.08 * (aptitude_score / 10)
    + 0.07 * (communication_score / 10)
    + 0.05 * (attendance / 10)
)

# Add some randomness
score = score + np.random.normal(0, 0.5, num_students)

# Convert score into placement outcome
threshold = np.median(score)

placed = (score >= threshold).astype(int)


# ---------------------------------------------------
# Generate company and package information
# ---------------------------------------------------

companies = [
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Cognizant",
    "Capgemini",
    "Deloitte",
    "Tech Mahindra"
]

company = []

package_lpa = []

for placement_status in placed:

    if placement_status == 1:
        selected_company = np.random.choice(companies)

        salary = np.round(
            np.random.uniform(3.0, 12.0),
            2
        )

        company.append(selected_company)
        package_lpa.append(salary)

    else:
        company.append("Not Placed")
        package_lpa.append(0)


# Placement year
placement_year = np.random.choice(
    [2024, 2025, 2026],
    size=num_students,
    p=[0.25, 0.30, 0.45]
)


# ---------------------------------------------------
# Create DataFrame
# ---------------------------------------------------

df = pd.DataFrame({
    "student_id": student_ids,
    "branch": branches,
    "cgpa": cgpa,
    "tenth_percentage": tenth_percentage,
    "twelfth_percentage": twelfth_percentage,
    "backlogs": backlogs,
    "internships": internships,
    "projects": projects,
    "certifications": certifications,
    "technical_skills": technical_skills,
    "aptitude_score": aptitude_score,
    "communication_score": communication_score,
    "attendance": attendance,
    "placed": placed,
    "company": company,
    "package_lpa": package_lpa,
    "placement_year": placement_year
})


# ---------------------------------------------------
# Save dataset
# ---------------------------------------------------

output_path = "data/raw/students_raw.csv"

df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print(f"Total students: {len(df)}")
print(f"Saved to: {output_path}")

print("\nFirst 5 records:")
print(df.head())

print("\nPlacement distribution:")
print(df["placed"].value_counts())