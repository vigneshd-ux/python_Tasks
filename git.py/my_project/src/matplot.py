import matplotlib.pyplot as plt

students = ["Arun", "Priya", "Kumar"]
marks = [75, 87, 90]

plt.pie(marks, labels=students, autopct="%1.1f%%", startangle=90)
plt.title("Each Student's Share of Total Marks")
plt.axis("equal")  # Keep the pie chart circular
plt.show()