import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


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
# 4. CREATE MODELS
# =========================================================

models = {

    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(random_state=42))
    ]),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss"
    )
}


# =========================================================
# 5. TRAIN AND EVALUATE
# =========================================================

results = []

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Probability for ROC-AUC
    y_probability = model.predict_proba(X_test)[:, 1]

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(y_test, y_pred)

    recall = recall_score(y_test, y_pred)

    f1 = f1_score(y_test, y_pred)

    roc_auc = roc_auc_score(y_test, y_probability)

    cm = confusion_matrix(y_test, y_pred)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC-AUC": roc_auc
    })

    print(f"{name} completed.")

    print("Confusion Matrix:")
    print(cm)


# =========================================================
# 6. RESULTS TABLE
# =========================================================

results_df = pd.DataFrame(results)

print("\n========== MODEL EVALUATION ==========")

print(results_df.to_string(index=False))


# =========================================================
# 7. BEST MODEL
# =========================================================

best_model = results_df.loc[
    results_df["F1 Score"].idxmax()
]

print("\n========== BEST MODEL ==========")

print("Best model:", best_model["Model"])
print("F1 Score:", round(best_model["F1 Score"], 3))

print("\nModel evaluation completed successfully!")