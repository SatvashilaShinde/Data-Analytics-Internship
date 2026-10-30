-- 1. Create Database
CREATE DATABASE StudentDB;
USE StudentDB;

-- 2. Create Department Table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

-- 3. Insert Department Records
INSERT INTO Departments VALUES
(1, 'IT'),
(2, 'Computer'),
(3, 'Mechanical');

-- 4. Create Student Table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    DepartmentID INT,
    Age INT,
    StudyHours INT,
    Marks INT,
    Attendance INT
);

-- 5. Insert Student Records
INSERT INTO Students VALUES
(1, 'Rahul', 1, 21, 4, 85, 90),
(2, 'Priya', 2, 22, 5, 92, 95),
(3, 'Amit', 1, 21, 2, 65, 75),
(4, 'Sneha', 2, 22, 6, 95, 98),
(5, 'Neha', 3, 23, 3, 70, 80),
(6, 'Akash', 1, 21, 1, 45, 60),
(7, 'Pooja', 2, 22, 5, 88, 92),
(8, 'Rohan', 3, 23, 2, 55, 70),
(9, 'Anjali', 1, 21, 4, 78, 85),
(10, 'Vijay', 2, 22, 3, 72, 78);

-- 6. Display All Students
SELECT * FROM Students;

-- 7. Filter Students
SELECT * FROM Students
WHERE Marks > 75;

-- 8. Sort Students by Marks
SELECT * FROM Students
ORDER BY Marks DESC;

-- 9. Aggregate Functions
SELECT
    COUNT(*) AS TotalStudents,
    AVG(Marks) AS AverageMarks,
    MAX(Marks) AS HighestMarks,
    MIN(Marks) AS LowestMarks
FROM Students;

-- 10. Group By Department
SELECT
    DepartmentID,
    AVG(Marks) AS AverageMarks
FROM Students
GROUP BY DepartmentID;

-- 11. Update Student Marks
UPDATE Students
SET Marks = 70
WHERE StudentID = 3;

-- 12. Join Two Tables
SELECT
    Students.Name,
    Departments.DepartmentName,
    Students.Marks
FROM Students
INNER JOIN Departments
ON Students.DepartmentID = Departments.DepartmentID;

-- 13. Delete One Student Record
DELETE FROM Students
WHERE StudentID = 10;

-- 14. Display Final Student Records
SELECT * FROM Students;
