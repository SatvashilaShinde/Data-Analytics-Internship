
# ==========================================
# PYTHON FOUNDATION ASSESSMENT
# ==========================================

# 1. Variables and Data Types
name = "Rahul"
age = 21
marks = 85.5
passed = True

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Passed:", passed)

# 2. Operators
a = 20
b = 10

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# 3. User Input
student_name = input("\nEnter student name: ")
student_marks = float(input("Enter marks: "))

print("Student:", student_name)
print("Marks:", student_marks)

# 4. If-Else Conditions
if student_marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

# 5. For Loop
print("\nMultiplication Table:")
for i in range(1, 6):
    print(5, "x", i, "=", 5 * i)

# 6. While Loop
count = 1
print("\nWhile Loop:")
while count <= 5:
    print(count)
    count += 1

# 7. Functions
def calculate_percentage(maths, science, english):
    total = maths + science + english
    return total / 3

percentage = calculate_percentage(80, 85, 90)
print("\nPercentage:", percentage)

# 8. List
marks_list = [80, 85, 90, 75, 95]

print("\nList:", marks_list)
print("Maximum:", max(marks_list))
print("Minimum:", min(marks_list))
print("Length:", len(marks_list))

marks_list.append(88)
print("After Append:", marks_list)

# 9. Tuple
subjects = ("Maths", "Science", "English")
print("\nTuple:", subjects)

# 10. Set
numbers = {10, 20, 20, 30, 40}
print("\nSet:", numbers)

# 11. Dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}

print("\nDictionary:", student)
print("Student Name:", student["name"])

# 12. Exception Handling
try:
    number = int(input("\nEnter a number: "))
    print("Number:", number)
except ValueError:
    print("Please enter a valid integer.")

print("\nPython Assessment Completed!")
