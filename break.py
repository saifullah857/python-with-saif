# password = "python123"

# while True:

#     user = input("Enter Password: ")

#     if user == password:
#         print("Login Successful")
#         break

#     print("Wrong Password")



# numbers = [7, 9, 11, 14, 16]
# index = 0

# while index < len(numbers):

#     if numbers[index] % 2 == 0:
#         print("First Even Number:", numbers[index])
#         break

#     index += 1


# secret = 8

# while True:

#     guess = int(input("Guess Number: "))

#     if guess == secret:
#         print("Correct Guess")
#         break

#     print("Try Again")

# while True:

#     number = int(input("Enter a number (0 to stop): "))

#     if number == 0:
#         break

#     print("You entered:", number)

# print("Loop Ended")


total = 0
count = 0

while True:

    number = int(input("Enter a number: "))

    total = total + number

    print("Current Total:", total)
    count += 1



    if total >= 50:
        break

print("Target Reached!")
print("Total attempts = ",count)



# correct_pin = 1234

# attempt = 1

# while attempt <= 3:

#     pin = int(input("Enter PIN: "))

#     if pin == correct_pin:
#         print("Access Granted")
#         break

#     print("Wrong PIN")

#     attempt += 1

# print("Program Ended")










































