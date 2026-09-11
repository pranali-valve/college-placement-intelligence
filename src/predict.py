import pandas as pd
import joblib


# =========================================================
# 1. LOAD SAVED MODEL
# =========================================================

model = joblib.load("models/placement_model.pkl")

features = joblib.load("models/feature_names.pkl")


# =========================================================
# 2. SAMPLE STUDENT
# =========================================================

student = {
    "cgpa": 8.5,
    "tenth_percentage": 85,
    "twelfth_percentage": 82,
    "backlogs": 0,
    "internships": 2,
    "projects": 3,
    "certifications": 3,
    "technical_skills": 7,
    "aptitude_score": 80,
    "communication_score": 78,
    "attendance": 90
}


# =========================================================
# 3. CREATE DATAFRAME
# =========================================================

student_df = pd.DataFrame([student])

student_df = student_df[features]


# =========================================================
# 4. MAKE PREDICTION
# =========================================================

prediction = model.predict(student_df)[0]

probability = model.predict_proba(student_df)[0][1]


# =========================================================
# 5. DISPLAY RESULT
# =========================================================

print("========== STUDENT PREDICTION ==========")

print("Prediction:", prediction)

print("Placement Probability:", round(probability * 100, 2), "%")


if prediction == 1:
    print("Result: PLACEMENT LIKELY")
else:
    print("Result: PLACEMENT RISK")


print("\nPrediction completed successfully!")