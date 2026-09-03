
# # # # # urdu = int(input("Enter ur urdu marks = "))
# # # # # englis = int(input("Enter ur urdu marks = "))
# # # # # math = int(input("Enter ur urdu marks = "))
# # # # # cmp = int(input("Enter ur urdu marks = "))
# # # # # stat = int(input("Enter ur urdu marks = "))
# # # # # isl = int(input("Enter ur urdu marks = "))



# # # # # percagtag = urdu + englis +stat +cmp + isl + math / 600 * 100

# # # # # print(percagtag)


# # # # # start = 1
# # # # # last = 10

# # # # # while start <= last:
# # # # #     if start % 2 == 0:
# # # # #         print(start)

# # # # # while start <= last:
# # # # #     if start % 2 == 0:
# # # # #         print(start)
# # # # #     start += 1  


# # # # # Input total number of subjects
# # # # total_subjects = int(input("Enter total number of subjects: "))

# # # # obtained_marks = 0
# # # # count = 1

# # # # # Input marks
# # # # while count <= total_subjects:
# # # #     marks = float(input(f"Enter marks of Subject {count}: "))
# # # #     obtained_marks += marks
# # # #     count += 1

# # # # # Calculate percentage
# # # # total_marks = total_subjects * 100
# # # # percentage = (obtained_marks / total_marks) * 100

# # # # # Grade
# # # # if percentage >= 80:
# # # #     grade = "A"
# # # # elif percentage >= 70:
# # # #     grade = "B"
# # # # elif percentage >= 60:
# # # #     grade = "C"
# # # # elif percentage >= 50:
# # # #     grade = "D"
# # # # else:
# # # #     grade = "Fail"

# # # # # Output
# # # # print("\n========== RESULT ==========")
# # # # print("Total Subjects :", total_subjects)
# # # # print("Total Marks    :", total_marks)
# # # # print("Obtained Marks :", obtained_marks)
# # # # print("Percentage     :", round(percentage, 2), "%")
# # # # print("Grade          :", grade)

# # # transactions = int(input("Enter number of deposits: "))

# # # count = 1
# # # balance = 0

# # # while count <= transactions:

# # #     amount = float(input(f"Deposit {count}: "))

# # #     if amount >= 10000:
# # #         print("Large Deposit")
# # #     elif amount >= 5000:
# # #         print("Medium Deposit")
# # #     else:
# # #         print("Small Deposit")

# # #     balance += amount
# # #     count += 1

# # # print("\n===== ACCOUNT SUMMARY =====")
# # # print("Final Balance :", balance)


# # # items = int(input("Enter total items: "))

# # # count = 1
# # # bill = 0

# # # while count <= items:

# # #     price = float(input(f"Price of Item {count}: "))

# # #     bill += price
# # #     count += 1

# # # if bill >= 20000:
# # #     discount = bill * 0.20
# # # elif bill >= 10000:
# # #     discount = bill * 0.10
# # # else:
# # #     discount = 0

# # # print("\n===== BILL =====")
# # # print("Total Bill :", bill)
# # # print("Discount   :", discount)
# # # print("Payable    :", bill - discount)




# # total_items = int(input("Enter no of items you wants to purchase = "))

# # counter = 1
# # bill = 0

# # while counter <= total_items:
# #     product = float(input(f"Enter product  {counter}  price = "))
    
# #     bill += product
# #     counter += 1
    
# # if bill >= 20_000:
# #     discount = bill * 0.20
# # elif bill >= 10_000:
# #     discount = bill * 0.10
# # else:
# #     discount = 0
    
# # print("="*10,"summury","="*10)
# # print(f"Total Items purchased items = {total_items}")
# # print(f"bills before discount = {bill}")
# # print(f" discount = {discount}")
# # print(f"bill after  discount = {bill - discount}")




# patients = int(input("Enter total patients = "))

# count = 1 

# while count <= patients:
#     weight = float(input("Enter your weight in KG = "))
#     height = float(input("Enter your height in (M) = "))
    
#     bmi = weight / height**2
    
#     print(f"your bmi value is ={bmi}")
    
    
#     if bmi >= 30:
#         print("Khata hi gull hai tera to")
#     elif bmi > 25:
#         print("Overweight hai tu")
#     elif bmi >= 18.5:
#         print("Normal")
#     else:
#         print("Underweight")
        
#     count += 1 


# str()


# name = input("tera naam kia hai = ")

# print("tera name yeah hai = ",name)


a = int(input("a ki value enter kr dy = "))
b = int(input("b ki value enter kr dy = "))

print("swap krny sy pehly a",a,"aur b",b)

c = 0

c = a # c = 10 -> a = 0
a = b # a = 5 -> b = 0 
b = c # b = 10 -> c =

print("swap krny sy baad a",a,"aur b",b)

print("value of a = ",a,"and value of b = ",b)
print(f"value of a = {a} and value of b = {b}")

