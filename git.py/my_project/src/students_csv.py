import pandas as pd

students = pd.read_csv("students.csv")

print("Student Details:")
print(students)

print("\nAverage Marks:", students["marks"].mean())

print("Maximum Marks:", students["marks"].max())

print("Minimum Marks:", students["marks"].min())

top_student = students.loc[students["marks"].idxmax()]

print("\nTop Student:")
print(top_student)