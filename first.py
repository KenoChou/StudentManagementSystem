students = []

def add_student():
    name = input("Enter student name: ")

    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("❌ Age must be a number!")
        return

    student = {
        "name": name,
        "age": age
    }

    students.append(student)
    print("✅ Student added successfully!")


def show_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for i, s in enumerate(students):
        print(f"{i+1}. Name: {s['name']}, Age: {s['age']}")


def delete_student():
    name = input("Enter name to delete: ")

    for s in students:
        if s["name"] == name:
            students.remove(s)
            print("🗑 Student deleted successfully!")
            return

    print("❌ Student not found.")


def search_student():
    name = input("Enter name to search: ")

    for s in students:
        if s["name"] == name:
            print(f"🎯 Found: Name: {s['name']}, Age: {s['age']}")
            return

    print("❌ Student not found.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        search_student()

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice, try again.")