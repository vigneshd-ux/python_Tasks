import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("employees.csv")


print("Employee Data:")
print(df)


print("\nTotal Employees:", len(df))

print("Average Salary:", df["salary"].mean())

print("Highest Salary:", df["salary"].max())

print("Lowest Salary:", df["salary"].min())


print("\nAverage Salary by Department:")

department_salary = df.groupby("department")["salary"].mean()

print(department_salary)


highest_salary_employee = df.loc[df["salary"].idxmax()]

print("\nHighest Paid Employee:")
print(highest_salary_employee)


plt.bar(df["name"], df["salary"])

plt.xlabel("Employee")
plt.ylabel("Salary")
plt.title("Employee Salary Analysis")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()