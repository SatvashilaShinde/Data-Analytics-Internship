
import pandas as pd
import matplotlib.pyplot as plt

# Read Student Dataset
df = pd.read_csv("dataset/student_data.csv")

# 1. Bar Chart - Department-wise Average Marks
department_marks = df.groupby("Department")["Marks"].mean()

plt.figure(figsize=(8, 5))
plt.bar(department_marks.index, department_marks.values)
plt.title("Department-wise Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()

# 2. Line Chart - Student-wise Marks
plt.figure(figsize=(8, 5))
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student-wise Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


print("Visualization Assessment Completed!")
