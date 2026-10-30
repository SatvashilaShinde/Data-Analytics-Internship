import pandas as pd
import numpy as np

# Read Student Dataset
df = pd.read_csv("dataset/student_data.csv")

marks = df["Marks"]

# 1. Mean
print("Mean:", marks.mean())

# 2. Median
print("Median:", marks.median())

# 3. Mode
print("Mode:", marks.mode().tolist())

# 4. Minimum and Maximum
print("Minimum Marks:", marks.min())
print("Maximum Marks:", marks.max())

# 5. Range
print("Range:", marks.max() - marks.min())

# 6. Variance
print("Variance:", marks.var())

# 7. Standard Deviation
print("Standard Deviation:", marks.std())

# 8. Percentile
print("75th Percentile:", np.percentile(marks, 75))

# 9. Correlation
correlation = df["StudyHours"].corr(df["Marks"])
print("Study Hours and Marks Correlation:", correlation)

print("\nStatistics Assessment Completed!")
