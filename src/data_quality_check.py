import pandas as pd


# Load dataset
df = pd.read_csv("data/raw/students_raw.csv")


# 1. Basic information
print("========== DATASET INFORMATION ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# 2. Column names
print("\n========== COLUMNS ==========")
print(df.columns.tolist())


# 3. Data types
print("\n========== DATA TYPES ==========")
print(df.dtypes)


# 4. Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# 5. Duplicate rows
print("\n========== DUPLICATE ROWS ==========")
print("Duplicate rows:", df.duplicated().sum())


# 6. Statistical summary
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# 7. Placement distribution
print("\n========== PLACEMENT DISTRIBUTION ==========")
print(df["placed"].value_counts())


# 8. Placement percentage
print("\n========== PLACEMENT PERCENTAGE ==========")
print(df["placed"].value_counts(normalize=True) * 100)