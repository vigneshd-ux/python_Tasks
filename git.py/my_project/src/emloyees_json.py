import json
employe = [
    {
        "id": 1,
        "name": "Vignesh",
        "age": 25,
        "salary": 30000
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 28,
        "salary": 40000
    },
    {
        "id": 3,
        "name": "Arun",
        "age": 30,
        "salary": 45000
    }
]

with open("employees.json.py", "r") as file:
    employees = json.load(file)

print("Employee Details:")

for employee in employees:
    print("ID:", employee["id"])
    print("Name:", employee["name"])
    print("Age:", employee["age"])
    print("Salary:", employee["salary"])
    print("----------------")