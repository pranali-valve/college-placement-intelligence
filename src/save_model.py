import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


# =========================================================
# 1. LOAD DATA
# =========================================================

df = pd.read_csv("data/raw/students_raw.csv")


# =========================================================
# 2. FEATURES AND TARGET
# =========================================================

features = [
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
    "attendance"
]

target = "placed"


X = df[features]
y = df[target]


# =========================================================
# 3. TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# =========================================================
# 4. CREATE BEST MODEL
# =========================================================

model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(random_state=42))
])


# =========================================================
# 5. TRAIN MODEL
# =========================================================

model.fit(X_train, y_train)


# =========================================================
# 6. SAVE MODEL
# =========================================================

joblib.dump(model, "models/placement_model.pkl")


# Save feature names
joblib.dump(features, "models/feature_names.pkl")


print("========== MODEL SAVING ==========")

print("Best model: Logistic Regression")
print("Model saved successfully!")
print("Location: models/placement_model.pkl")

print("\nFeature names saved successfully!")
print("Location: models/feature_names.pkl")