# Student Management System

students = {
    101: {
        "name": "Ali",
        "age": 20,
        "course": "AI",
        "marks": 90
    },

    102: {
        "name": "Sara",
        "age": 21,
        "course": "Data Science",
        "marks": 88
    },

    103: {
        "name": "Ahmed",
        "age": 22,
        "course": "Python",
        "marks": 95
    }
}


while True:

    print("\n========= STUDENT MANAGEMENT SYSTEM =========")

    print("Available Student IDs:", list(students.keys()))

    student_id = int(input("Enter Student ID: "))

    student = students.get(student_id)

    if student is None:
        print("Student Not Found!")
        break

    print("""
1. Get Value
2. Show Keys
3. Show Values
4. Show Items
5. Update Information
6. Remove Key (pop)
7. Remove Last Item (popitem)
8. Clear Student Record
9. Set Default Value
10. Exit
""")

    choice = int(input("Enter your choice: "))

    # -----------------------------------------
    if choice == 1:

        key = input("Enter key to search: ")

        print(student.get(key, "Key Not Found"))

    # -----------------------------------------
    elif choice == 2:

        print("\nKeys are:")
        print(student.keys())

    # -----------------------------------------
    elif choice == 3:

        print("\nValues are:")
        print(student.values())

    # -----------------------------------------
    elif choice == 4:

        print("\nStudent Record")

        for key, value in student.items():
            print(f"{key} : {value}")

    # -----------------------------------------
    elif choice == 5:

        key = input("Enter key to update: ")
        value = input("Enter new value: ")

        student.update({key: value})

        print("\nRecord Updated Successfully!")
        print(student)

    # -----------------------------------------
    elif choice == 6:

        key = input("Enter key to remove: ")

        removed = student.pop(key, "Key Not Found")

        print("Removed Value:", removed)

        print(student)

    # -----------------------------------------
    elif choice == 7:

        if len(student) > 0:

            removed = student.popitem()

            print("Removed:", removed)

        else:

            print("Dictionary is Empty.")

        print(student)

    # -----------------------------------------
    elif choice == 8:

        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":

            student.clear()

            print("Student Record Cleared!")

        print(student)

    # -----------------------------------------
    elif choice == 9:

        key = input("Enter key: ")
        default = input("Enter default value: ")

        student.setdefault(key, default)

        print(student)

    # -----------------------------------------
    elif choice == 10:

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")