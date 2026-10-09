name = input("Enter student name: ")
age = input("Enter student age: ")
marks = input("Enter student marks: ")

with open("students.txt", "w") as file:
    file.write("Student Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Marks: " + marks + "\n")

print("Student details saved successfully!")