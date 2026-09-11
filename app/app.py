import sys
import os

import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PROJECT ROOT PATH
# =========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# =========================================================
# IMPORT STUDENT INTELLIGENCE
# =========================================================

from src.student_intelligence import (
    analyze_student,
    get_student_status
)

from src.database_data import get_all_student_data


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="College Placement Intelligence",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load(
    os.path.join(PROJECT_ROOT, "models", "placement_model.pkl")
)

features = joblib.load(
    os.path.join(PROJECT_ROOT, "models", "feature_names.pkl")
)


# =========================================================
# TITLE
# =========================================================

st.title("🎓 College Placement Intelligence System")

st.write(
    "Predict student placement probability using Machine Learning."
)

st.divider()


# =========================================================
# STUDENT PREDICTION
# =========================================================

st.header("👨‍🎓 Student Prediction")


# =========================================================
# STUDENT NAME
# =========================================================

student_name = st.text_input(
    "Student Name"
)


# =========================================================
# INPUT FEATURES
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.5,
        step=0.01
    )

    tenth_percentage = st.number_input(
        "10th Percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.1
    )

    twelfth_percentage = st.number_input(
        "12th Percentage",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.1
    )

    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )


with col2:

    internships = st.number_input(
        "Internships",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

    projects = st.number_input(
        "Projects",
        min_value=0,
        max_value=10,
        value=2,
        step=1
    )

    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )

    technical_skills = st.number_input(
        "Technical Skills",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )


with col3:

    aptitude_score = st.number_input(
        "Aptitude Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.1
    )

    communication_score = st.number_input(
        "Communication Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.1
    )

    attendance = st.number_input(
        "Attendance",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        step=0.1
    )


st.divider()


# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button(
    "🔮 Predict Placement",
    use_container_width=True
):

    # =====================================================
    # CREATE STUDENT DATA
    # =====================================================

    student = {
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
        "attendance": attendance
    }


    # =====================================================
    # CREATE DATAFRAME
    # =====================================================

    student_df = pd.DataFrame(
        [student]
    )

    student_df = student_df[features]


    # =====================================================
    # ML PREDICTION
    # =====================================================

    prediction = model.predict(
        student_df
    )[0]

    probability = model.predict_proba(
        student_df
    )[0][1]

    probability_percentage = probability * 100


    # =====================================================
    # PREDICTION RESULT
    # =====================================================

    st.divider()

    st.header("📊 Prediction Result")


    if prediction == 1:

        st.success(
            "🟢 Placement Likely"
        )

    else:

        st.warning(
            "🟠 Placement Risk"
        )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Placement Probability",
            f"{probability_percentage:.2f}%"
        )


    with col2:

        if prediction == 1:
            result = "Placed"
        else:
            result = "Not Placed"

        st.metric(
            "Prediction",
            result
        )


    if student_name:

        st.info(
            f"Prediction generated for **{student_name}**."
        )


    # =====================================================
    # STUDENT INTELLIGENCE
    # =====================================================

    analysis = analyze_student(
        student
    )


    st.divider()

    st.header("🧠 Student Intelligence")


    # =====================================================
    # STRONG AREAS
    # =====================================================

    st.subheader("💪 Strong Areas")


    if analysis["strengths"]:

        for strength in analysis["strengths"]:

            st.write(
                f"✅ {strength}"
            )

    else:

        st.write(
            "No major strengths identified yet."
        )


    # =====================================================
    # SKILL GAPS
    # =====================================================

    st.subheader("📈 Areas to Improve")


    if analysis["skill_gaps"]:

        for gap in analysis["skill_gaps"]:

            st.write(
                f"⚠️ {gap}"
            )

    else:

        st.write(
            "No major improvement areas identified."
        )


    # =====================================================
    # RECOMMENDED ROLES
    # =====================================================

    st.subheader("🎯 Recommended Roles")


    for role in analysis["recommended_roles"]:

        st.write(
            f"💼 {role}"
        )


    # =====================================================
    # STUDENT STATUS
    # =====================================================

    st.subheader("📌 Student Status")


    status = analysis["status"]


    if status == "Placement Ready":

        st.success(
            "🟢 Placement Ready"
        )

    elif status == "High Risk":

        st.error(
            "🔴 High Risk"
        )

    else:

        st.warning(
            "🟠 Needs Training"
        )


# =========================================================
# ADMIN DASHBOARD
# =========================================================

st.divider()

st.header("📊 Admin Dashboard")


# =========================================================
# LOAD COMPLETE DATASET FROM POSTGRESQL
# =========================================================

try:

    admin_df = get_all_student_data()

except Exception as e:

    st.error(
        "Unable to load student data from PostgreSQL."
    )

    st.exception(e)

    st.stop()


# =========================================================
# STUDENT STATUS ANALYSIS
# =========================================================

admin_df["student_status"] = admin_df.apply(
    get_student_status,
    axis=1
)


# =========================================================
# FILTER SECTION
# =========================================================

st.subheader("🔎 Filters")


filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)


# =========================================================
# BRANCH FILTER
# =========================================================

with filter_col1:

    branch_options = [
        "All"
    ] + sorted(
        admin_df["branch"].dropna().unique().tolist()
    )

    selected_branch = st.selectbox(
        "Branch",
        branch_options
    )


# =========================================================
# PLACEMENT STATUS FILTER
# =========================================================

with filter_col2:

    placement_status_options = [
        "All",
        "Placed",
        "Not Placed"
    ]

    selected_placement_status = st.selectbox(
        "Placement Status",
        placement_status_options
    )


# =========================================================
# YEAR FILTER
# =========================================================

with filter_col3:

    year_options = [
        "All"
    ] + sorted(
        admin_df["placement_year"].dropna().unique().tolist()
    )

    selected_year = st.selectbox(
        "Placement Year",
        year_options
    )


# =========================================================
# STUDENT STATUS FILTER
# =========================================================

with filter_col4:

    student_status_options = [
        "All",
        "Placement Ready",
        "Needs Training",
        "High Risk"
    ]

    selected_student_status = st.selectbox(
        "Student Status",
        student_status_options
    )


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = admin_df.copy()


if selected_branch != "All":

    filtered_df = filtered_df[
        filtered_df["branch"] == selected_branch
    ]


if selected_placement_status == "Placed":

    filtered_df = filtered_df[
        filtered_df["placed"] == 1
    ]

elif selected_placement_status == "Not Placed":

    filtered_df = filtered_df[
        filtered_df["placed"] == 0
    ]


if selected_year != "All":

    filtered_df = filtered_df[
        filtered_df["placement_year"] == selected_year
    ]


if selected_student_status != "All":

    filtered_df = filtered_df[
        filtered_df["student_status"] == selected_student_status
    ]


# =========================================================
# FILTERED DATA MESSAGE
# =========================================================

st.caption(
    f"Showing {len(filtered_df)} students based on selected filters."
)


# =========================================================
# BASIC KPI CALCULATIONS
# =========================================================

total_students = len(
    filtered_df
)


placed_students = filtered_df[
    "placed"
].sum()


if total_students > 0:

    placement_rate = (
        placed_students / total_students
    ) * 100

else:

    placement_rate = 0


placed_df = filtered_df[
    filtered_df["placed"] == 1
]


if len(placed_df) > 0:

    average_package = placed_df[
        "package_lpa"
    ].mean()

    highest_package = placed_df[
        "package_lpa"
    ].max()

else:

    average_package = 0

    highest_package = 0


# =========================================================
# STUDENT STATUS COUNTS
# =========================================================

placement_ready = (
    filtered_df["student_status"] == "Placement Ready"
).sum()


needs_training = (
    filtered_df["student_status"] == "Needs Training"
).sum()


high_risk = (
    filtered_df["student_status"] == "High Risk"
).sum()


# =========================================================
# MAIN KPI CARDS
# =========================================================

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "Total Students",
        total_students
    )


with col2:

    st.metric(
        "Placed Students",
        placed_students
    )


with col3:

    st.metric(
        "Placement Rate",
        f"{placement_rate:.2f}%"
    )


with col4:

    st.metric(
        "Average Package",
        f"{average_package:.2f} LPA"
    )


with col5:

    st.metric(
        "Highest Package",
        f"{highest_package:.2f} LPA"
    )


# =========================================================
# STUDENT READINESS
# =========================================================

st.divider()

st.subheader("🎯 Student Readiness")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Placement Ready",
        placement_ready
    )


with col2:

    st.metric(
        "Needs Training",
        needs_training
    )


with col3:

    st.metric(
        "High Risk",
        high_risk
    )


# =========================================================
# BRANCH-WISE PLACEMENT
# =========================================================

st.divider()

st.subheader(
    "📈 Branch-wise Placement Rate"
)


if len(filtered_df) > 0:

    branch_placement = (
        filtered_df
        .groupby("branch")["placed"]
        .mean()
        .mul(100)
        .round(2)
    )

    st.bar_chart(
        branch_placement
    )


# =========================================================
# YEAR-WISE PLACEMENT
# =========================================================

st.subheader(
    "📅 Year-wise Placement Rate"
)


if len(filtered_df) > 0:

    year_placement = (
        filtered_df
        .groupby("placement_year")["placed"]
        .mean()
        .mul(100)
        .round(2)
    )

    st.line_chart(
        year_placement
    )


# =========================================================
# SALARY DISTRIBUTION
# =========================================================

st.subheader(
    "💰 Salary Distribution"
)


if len(placed_df) > 0:

    salary_data = placed_df[
        "package_lpa"
    ]

    st.bar_chart(
        salary_data.value_counts()
        .sort_index()
    )

else:

    st.info(
        "No placed students available for the selected filters."
    )


# =========================================================
# COMPANY HIRING
# =========================================================

st.subheader(
    "🏢 Company Hiring"
)


if len(placed_df) > 0:

    company_hiring = (
        placed_df["company"]
        .value_counts()
    )

    st.bar_chart(
        company_hiring
    )

else:

    st.info(
        "No company hiring data available for the selected filters."
    )


# =========================================================
# PLACEMENT STATUS
# =========================================================

st.subheader(
    "🎯 Placement Status"
)


status_data = pd.Series({
    "Placed": placed_students,
    "Not Placed": total_students - placed_students
})


st.bar_chart(
    status_data
)


# =========================================================
# STUDENT STATUS TABLE
# =========================================================

st.divider()

st.subheader(
    "👨‍🎓 Student Status"
)


status_table = filtered_df[
    [
        "student_id",
        "branch",
        "cgpa",
        "backlogs",
        "internships",
        "projects",
        "technical_skills",
        "student_status"
    ]
]


st.dataframe(
    status_table,
    use_container_width=True,
    hide_index=True
)
# =========================================================
# DOWNLOAD FILTERED STUDENT DATA
# =========================================================

csv_data = status_table.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Filtered Student Data",
    data=csv_data,
    file_name="filtered_student_data.csv",
    mime="text/csv",
    use_container_width=True
)