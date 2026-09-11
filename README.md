# 🎓 College Placement Intelligence System

A data-driven college placement analytics and prediction system that combines
Machine Learning, PostgreSQL, Streamlit, and Power BI to analyze student
profiles and support placement-related decision making.

---

## 📌 Project Overview

The College Placement Intelligence System is designed to help colleges
understand student placement trends and identify students who may need
additional training or support.

The system analyzes academic performance, technical skills, internships,
projects, aptitude, communication skills, attendance, and backlogs.

It provides:

- Placement prediction
- Placement probability
- Student intelligence analysis
- Strong areas
- Skill gaps
- Recommended job roles
- Student readiness classification
- Admin-level placement analytics
- Interactive Power BI dashboards
- PostgreSQL-based data storage

---

## 🎯 Problem Statement

Colleges generate a large amount of student and placement data, but this
data is often difficult to use for proactive placement planning.

The objective of this project is to build a system that can:

1. Analyze student placement data.
2. Identify factors associated with placement outcomes.
3. Predict placement likelihood using Machine Learning.
4. Identify students who are placement-ready.
5. Identify students who may require additional training.
6. Provide actionable insights through dashboards.

---

## 🚀 Key Features

### 👨‍🎓 Student Prediction

Students can enter their profile information including:

- CGPA
- 10th Percentage
- 12th Percentage
- Backlogs
- Internships
- Projects
- Certifications
- Technical Skills
- Aptitude Score
- Communication Score
- Attendance

The Machine Learning model provides:

- Placement prediction
- Placement probability
- Placement status

> The predicted probability is a model estimate and should not be treated
> as a guarantee of placement.

---

### 🧠 Student Intelligence

The system analyzes an individual student's profile and identifies:

#### Strong Areas

Examples:

- Strong academic performance
- Strong technical skills
- Good internship experience
- Good project experience
- Good aptitude score
- Good communication skills
- Good attendance
- No backlogs

#### Skill Gaps

Examples:

- Improve CGPA
- Improve technical skills
- Gain internship experience
- Build more projects
- Improve aptitude score
- Improve communication skills
- Clear backlogs

#### Recommended Roles

The system can recommend roles such as:

- Software Developer
- Data Analyst
- Business Analyst
- Machine Learning / AI Engineer
- Graduate Trainee

---

## 📊 Student Readiness Classification

Students are classified into three categories:

### 🟢 Placement Ready

Students who meet strong academic, technical, internship, and backlog
conditions.

### 🟡 Needs Training

Students who have potential but may need improvement in specific areas.

### 🔴 High Risk

Students with lower academic performance or a higher number of backlogs.

---

# 🤖 Machine Learning

## Dataset

The project uses a generated/simulated dataset containing:

- 1,250 student records
- 17 columns
- 11 prediction features
- 1 target variable

### Prediction Features

```text
cgpa
tenth_percentage
twelfth_percentage
backlogs
internships
projects
certifications
technical_skills
aptitude_score
communication_score
attendance
Target
placed
🔬 Models Evaluated

The following Machine Learning models were compared:

Logistic Regression
Decision Tree
Random Forest
XGBoost

The models were evaluated using:

Accuracy
Precision
Recall
F1-Score
ROC-AUC
Confusion Matrix
📈 Model Performance

The evaluation was performed on a held-out test set containing 20% of the
dataset.

Model	Accuracy	Precision	Recall	F1-Score	ROC-AUC
Logistic Regression	77.20%	76.98%	77.60%	77.29%	0.870
Decision Tree	69.20%	70.00%	67.20%	68.57%	0.692
Random Forest	74.40%	76.52%	70.40%	73.33%	0.827
XGBoost	74.00%	73.08%	76.00%	74.51%	0.815
🏆 Selected Model

Based on the evaluation results, Logistic Regression was selected as
the final model.

It achieved:

Accuracy: 77.20%
F1-Score: 77.29%
ROC-AUC: 0.870

These results are specific to the generated dataset and held-out test set.
They should not be interpreted as guaranteed real-world performance.

🔍 Feature Selection

The following features were used for pre-placement prediction:

CGPA
10th Percentage
12th Percentage
Backlogs
Internships
Projects
Certifications
Technical Skills
Aptitude Score
Communication Score
Attendance

Company and package information were not used as prediction features because
they are placement outcomes and would cause data leakage in a pre-placement
prediction scenario.

🗄️ PostgreSQL Database

The project uses PostgreSQL for persistent data storage.

Database
college_placement
Main Tables
students
placements
Students Table

Stores student profile information such as:

Student ID
Branch
CGPA
Academic percentages
Backlogs
Internships
Projects
Certifications
Technical Skills
Aptitude Score
Communication Score
Attendance
Placement Year
Placements Table

Stores:

Student ID
Placement status
Company
Package

The two tables are connected using:

student_id
🌐 Streamlit Application

The project includes a Streamlit web application.

The application provides:

Student Prediction

Students can enter their profile and receive a placement prediction.

Student Intelligence

The system provides:

Strong areas
Skill gaps
Recommended roles
Student status
Admin Dashboard

The admin dashboard provides:

Total students
Placement statistics
Average package
Highest package
Branch-wise analysis
Year-wise analysis
Company hiring analysis
Student readiness
Filtered student data
CSV export

The Admin Dashboard reads student data from PostgreSQL.

📊 Power BI Dashboard

The project includes interactive Power BI dashboards connected to
PostgreSQL.

Page 1 — Executive Overview

Contains:

Total Students
Placement Rate
Average Package
Highest Package
Placement Status
Placement Rate by Branch
Placement Trend by Year
Average Package by Branch
Interactive filters
Page 2 — Student Intelligence

Contains:

Placement Ready
Needs Training
High Risk
Placement by CGPA Range
Placement by Technical Skills
Placement by Internships
Placement by Projects
Placement by Aptitude Score Range
Placement by Communication Score Range
Placement Rate by Branch
Placement Trend by Year
Placement Status by Branch

🏗️ Project Architecture
                    ┌─────────────────────┐
                    │   Streamlit App     │
                    │  Student / Admin    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Python Backend      │
                    │ Prediction +        │
                    │ Intelligence        │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
       ┌──────────────────┐        ┌──────────────────┐
       │ Machine Learning │        │   PostgreSQL     │
       │ Model            │        │   Database       │
       └──────────────────┘        └────────┬─────────┘
                                            │
                                            ▼
                                  ┌──────────────────┐
                                  │     Power BI     │
                                  │    Dashboards    │
                                  └──────────────────┘

📁 Project Structure
college-placement-intelligence/
│
├── data/
│   ├── raw/
│   │   └── students_raw.csv
│   │
│   └── processed/
│
├── notebooks/
│   ├── 01_data_analysis.ipynb
│   ├── 02_eda.ipynb
│   └── 03_model_training.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predict.py
│   ├── student_intelligence.py
│   ├── database_connection.py
│   ├── database_queries.py
│   ├── database_data.py
│   ├── generate_data.py
│   ├── data_quality_check.py
│   ├── validate_data.py
│   ├── load_database.py
│   ├── save_model.py
│   └── utils.py
│
├── models/
│   ├── placement_model.pkl
│   └── feature_names.pkl
│
├── database/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── powerbi/
│
├── app/
│   └── app.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore

🛠️ Technology Stack
Technology	Purpose
Python	Backend and Machine Learning
Pandas	Data processing
NumPy	Numerical operations
Scikit-learn	Machine Learning
XGBoost	Machine Learning comparison
Matplotlib	Data visualization
Seaborn	Exploratory Data Analysis
Streamlit	Web application
PostgreSQL	Database
SQLAlchemy	Database connection
psycopg2	PostgreSQL driver
Joblib	Model persistence
Power BI	Business intelligence
Jupyter Notebook	Data analysis
🔐 Data Security

Database credentials are stored using environment variables.

The .env file is intentionally excluded from Git using .gitignore.

Example:

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=college_placement

Never upload the actual .env file or database password to GitHub.

▶️ How to Run the Project
1. Clone the Repository
git clone https://github.com/pranali-valve/college-placement-intelligence.git

Move into the project:

cd college-placement-intelligence
2. Install Dependencies
pip install -r requirements.txt
3. Configure PostgreSQL

Create a PostgreSQL database:

college_placement

Create the required tables using:

database/schema.sql
4. Configure Environment Variables

Create a .env file in the project root:

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=college_placement
5. Generate / Load Data

The generated dataset can be created using:

python src/generate_data.py

Database loading can be performed using:

python src/load_database.py
6. Run the Streamlit Application
streamlit run app/app.py

The application will open in the browser.

🧪 Data Quality & Validation

Before model development, the dataset was checked for:

Missing values
Duplicate records
Invalid CGPA values
Invalid percentage values
Invalid backlog values
Invalid attendance values
Invalid aptitude scores
Invalid communication scores
Invalid placement values
Invalid company/placement combinations
Invalid package/placement combinations

The generated dataset passed the validation checks successfully.

📌 Important Data Note

This project currently uses a synthetic/simulated dataset created for
development and demonstration purposes.

Therefore:

Model performance is specific to this dataset.
Placement probability is a model estimate.
The system should not be used as a guaranteed placement decision tool.
Real college data would be required for production deployment.
🔮 Future Enhancements

Possible future improvements include:

Student login and authentication
Admin authentication
Student profile management
CRUD operations
Resume analysis
Skill recommendation engine
Course recommendation
Company recommendation
Automated email notifications
Real-time placement updates
Cloud deployment
REST API using FastAPI
React frontend
Advanced ML model tuning
Model monitoring
Real college placement dataset integration
💡 Business Value

The system can help colleges move from simple placement reporting toward
data-driven placement planning.

Potential use cases include:

Identifying students who need training
Understanding placement trends
Monitoring placement readiness
Identifying skill gaps
Supporting placement cell decision making
Understanding branch-wise placement performance
Analyzing hiring patterns
Supporting student career guidance
🎓 Learning Outcomes

Through this project, the following concepts were implemented:

Python programming
Data generation
Data cleaning
Data validation
Exploratory Data Analysis
Feature engineering
Train/test splitting
Machine Learning model comparison
Model evaluation
Model persistence
Prediction pipelines
PostgreSQL database design
SQL queries
SQLAlchemy
Streamlit application development
Power BI dashboard development
Data-driven decision making

👩‍💻 Author

Pranali Valve

College Placement Intelligence System

⭐ Project Highlights
✔ Machine Learning
✔ Student Placement Prediction
✔ Student Intelligence
✔ PostgreSQL Database
✔ Streamlit Web Application
✔ Power BI Dashboards
✔ Data Quality & Validation
✔ Admin Analytics
✔ CSV Export
✔ End-to-End Data Pipeline
📄 Disclaimer

This project is developed for educational, portfolio, and demonstration
purposes. The placement predictions and probabilities generated by the
Machine Learning model are estimates based on the available dataset and
should not be considered guaranteed placement outcomes.