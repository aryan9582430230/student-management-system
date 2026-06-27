students = {}

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    students[name] = marks
    print("Student added successfully!")

def view_students():
    for name, marks in students.items():
        print(name, marks)

while True:
    print("1 Add Student")
    print("2 View Students")
    print("3 Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
