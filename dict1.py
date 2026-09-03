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
    print("="*10,"Student Management System","="*10)
    print(f"Available ID,s are = {list(students.keys())}")
    
    std_id = int(input("Select any ID = "))
    student = students.get(std_id)
    if student is None:
        print(f"Student with this ID = {std_id} not exisit")
        break
    
        
    print("""
        Can Perform one of these following Operations on this student data \n
        1 - Get Values
        2 - Show Keys
        3 - Show Values
        4 - Get Full Record
        5 - Update Record
        6 - Romove Any key
        7 - Remove Last one
        8 - Clear Student Record
        9 - Add Additional Data
        10 - Exit
        """)
    choice = int(input("Enter your choice = "))
    if choice == 1:
        print(f" keys = {list(student.keys())}")
        key = input("Enter any key to get value = ")
        print(student.get(key,"Not found"))
        
    elif choice == 2:
        print("="*2,"All keys are ","="*2)
        print(list(student.keys()))
        
    elif choice == 3:
        print("="*2,"All values are ","="*2)
        print(list(student.values()))
        
    elif choice == 4:
        print("="*5,"Student Record","="*5)
        for key,value in student.items():
            
            print(f"{key} : {value}")
    elif choice == 5:
        print(f"enter key and values to update from following  \n \n {list(student.keys())} keys")
        key = input("Enter key = ")
        value = input("Enter value = ")
        student.update({key:value})
        print("\n Updated Successfully ")
        print(student)
    elif choice == 6:
        conform = input("Sure yes / no = ")
        if conform.lower() == "yes":
            print(f"keys = {list(student.keys())}")
            key = input("Enter key to Remove = ")
            student.pop(key)
            print("Removed Successfully")
            print(student)
        else:
            print(student)
    elif choice == 7:
        conform = input("Are sure to delete last one yes / no =")
        if conform.lower() == "yes":
            student.popitem()
            print("Last key Removed")
            print(student)
        else:
            print(student)
    elif choice == 8:
        conform = input("Are youe sure yes / no =")
        if conform.lower() == "yes":
            student.clear()
            print("Cleared successfully")
        else:
            print("Invalid input")
        
    elif choice == 9:
        print(f"Add data in this information \n {student}")
        new_key = input("Enter new key = ")
        new_value = input("Enter new value = ")
        student.update({new_key : new_value})
        print("Added new Data Successfully")
        print(student)
        
    elif choice == 10:
        break
    
    else:
        print("Invalid choice")
        
        
    break


