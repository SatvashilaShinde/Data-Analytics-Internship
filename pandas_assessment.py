
# ==========================================
# PANDAS FOUNDATION ASSESSMENT
# Student Data Analysis
# ==========================================

import pandas as pd

# 1. Read CSV File
df = pd.read_csv("dataset/student_data.csv")

# 2. Display First 5 Records
print("\nStudent Data:")
print(df.head())

# 3. Display Dataset Information
print("\nDataset Information:")
df.info()

# 4. Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# 5. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 6. Remove Extra Spaces from Names
df["Name"] = df["Name"].str.strip()

# 7. Filter Students Scoring Above 75
print("\nStudents Scoring Above 75:")
print(df[df["Marks"] > 75])

# 8. Sort Students by Marks
print("\nStudents Sorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

# 9. Average Marks Department-wise
print("\nDepartment-wise Average Marks:")
print(df.groupby("Department")["Marks"].mean())

# 10. Count Students in Each Department
print("\nDepartment-wise Student Count:")
print(df["Department"].value_counts())

print("\nPandas Assessment Completed!")
