def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{sid},{name},{marks}\n")

    print("Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if not students:
            print("No students found.")
        else:
            print("\n--- Student List ---")
            for student in students:
                sid, name, marks = student.strip().split(",")
                print(f"ID: {sid}, Name: {name}, Marks: {marks}")

    except FileNotFoundError:
        print("No students file found.")


def search_student():
    search_id = input("Enter Student ID to search: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                sid, name, marks = line.strip().split(",")
                if sid == search_id:
                    print(f"Found -> ID: {sid}, Name: {name}, Marks: {marks}")
                    found = True

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No students file found.")


def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    found = False
    students = []

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        with open("students.txt", "w") as file:
            for line in students:
                sid, name, marks = line.strip().split(",")
                if sid != delete_id:
                    file.write(line)
                else:
                    found = True

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No students file found.")


while True:
    print("\n--- Student Management System developed by Monty---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
