
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Home
@app.get("/")
def home():
    return {
        "message": "Student API is running"
    }


# Student model
class Student(BaseModel):
    name: str
    age: int


# Student data
students = [
    {"id": 1, "name": "Rahul", "age": 20},
    {"id": 2, "name": "Priya", "age": 22},
    {"id": 3, "name": "Arun", "age": 23}
]


# GET - Get all students
@app.get("/students")
def get_students():
    return students


# POST - Create a student
@app.post("/students")
def create_student(student: Student):

    new_id = len(students) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age
    }

    students.append(new_student)

    return {
        "message": "Student created successfully",
        "student": new_student
    }


# DELETE - Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted successfully",
                "student": student
            }

    return {
        "message": "Student not found"
    }


# PUT - Update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    for s in students:

        if s["id"] == student_id:

            s["name"] = student.name
            s["age"] = student.age

            return {
                "message": "Student updated successfully",
                "student": s
            }

    return {
        "message": "Student not found"
    }


# Run the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
