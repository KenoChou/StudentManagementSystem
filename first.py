students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")

        student = {
            "name": name,
            "age": age
        }

        students.append(student)
        print("Student added successfully!")

    # Show Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n--- Student List ---")
            for i, s in enumerate(students):
                print(f"{i+1}. Name: {s['name']}, Age: {s['age']}")

    # Exit
    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid choice, try again.")