import pandas as pd


# Load dataset
df = pd.read_csv("data/raw/students_raw.csv")


# Features used for prediction
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


# Target variable
target = "placed"


# Create X and y
X = df[features]
y = df[target]


print("========== FEATURE ENGINEERING ==========")

print("Features:")
print(X.columns.tolist())

print("\nFeature shape:", X.shape)
print("Target shape:", y.shape)

print("\nTarget distribution:")
print(y.value_counts())

print("\nFeature engineering completed successfully!")