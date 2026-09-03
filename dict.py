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
    
    print(f"\n{"=" * 10} Student Management System {"=" * 10}\n")
    
    print(f"Available student ID,s = {list(students.keys())}")
    
    std_id = int(input("Enter student id = "))
    student = students.get(std_id)
    
    if student is None:
        print(f"Student with this id = {std_id} is not exist")
        break

    print("""
        1 - Get Keys
        2 - Get Values
        3 - Get Items
        4 - Update Information
        5 - Remove Key (pop)
        6 - Remove Last Item (popItem)
        7 - Clear Student Record
        8 - Exit
        """)
    choice = int(input("Enter Your choice = "))
    
    if choice == 1:
        
        print(f"All keys of student_id = {std_id} : \n {list(student.keys())}")
    
    elif choice == 2:
        print(f"All values of student_id = {std_id} : \n {list(student.values())}")
        
    elif choice == 3:
        print(f"Record of Student = {std_id} : \n ")
        
        for  key,value in student.items():
            print(f"{key} : {value}")
            
    elif choice == 4:
        print(f"According to these keys : {list(student.keys())} updates allowed")
        key = input("Enter key to update = ")
        value = input("Enter value to update = ")
        
        student.update({key : value})
        print(f"\n student \n")
    elif choice == 5:
    
        key = input("Enter key to remove: ")
        removed = student.pop(key, "Key Not Found")
        print("Removed Value:", removed)
        print(student)
    elif choice == 6:
    
        if len(student) > 0:

            removed = student.popitem()

            print("Removed:", removed)

        else:

            print("Dictionary is Empty.")

        print(student)
        
    elif choice == 7:
    
        confirm = input("Are you sure? (yes/no): ")
        if confirm.lower() == "yes":
            student.clear()
            print("Student Record Cleared!")
        print(student)
    elif choice == 10:
    
        print("Thank You!")
        break
    
    else:
    
        print("Invalid Choice!")
    
    break
    
        










        