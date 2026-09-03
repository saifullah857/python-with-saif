# num = 0                                                 
# while num<= 10:
#     if num == 5:
#         continue
#     num +=1
#     print(num)



# # skip current iteration and go to next iteratin

# # count = 1

# # while count <= 5:


# #     number = int(input("Enter a number: "))

# #     if number < 0:
# #         print("Negative number skipped")
# #         count += 1
# #         continue

# #     print("You entered:", number)

# #     count += 1




# # i = 1

# # while i <= 10:
    
# #     if i % 3 == 0:
# #         i += 1
# #         continue
# #     print(i)
# #     i += 1
    
# # i = 0

# # while i < 10:
# #     i += 1
# # #     if i % 2 == 0:
# # #         continue
# # #     print(i)
    
    
# # i = 1
# # vovel = 0

# # while i<= 10:
# #     ch = str(input("Enter any character or vovel = "))
# #     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
# #         vovel += 1
# #     i += 1
# # print("Total vovels ", vovel)
    
# # print("hello world")   



# print("saif ullah khalid")
# print('saif ullah khalid')


# # print("pakistan zindabad")



# num = float(input("Enter any floating num = "))

# print(num) # 78.67

# int_num = int(num) # 78.67 => 78
# float_num = num - int_num # 78.67 - 78 => 0.67
# print(int_num)
# print(float_num)





# print("my name is ------", "i have obtained marks = ",450,"total marks was = ",550,"in per = ",80)

# num_01 = int(input("Enter 1st num = "))
# num_02 = int(input("Enter 2nd num = "))

# print("="*10,"Befor swaping","="*10)
# print("1st num is = ",num_01)
# print("2nd num is = ",num_02)

# num_01 , num_02 = num_02 , num_01

# print("="*10,"after swaping","="*10)
# print("1st num is = ",num_01)
# print("2nd num is = ",num_02)


# sum = 0
# count = 0

# while True:
#     num = int(input("Enter a num = "))
#     sum += num
#     print("Total sum = ",sum)
#     count += 1
#     if sum >= 500:
#         break
# print("You accesds limits")
# print("in attempts = ",count)



password = "123abc"
# while True:
#     user_pass = input("Enter your password = ")
#     if user_pass == password:
#         print(user_pass," correct password")
#         break
#     print(user_pass," is wrong")

#------------------------------- sevice page ----------------

for num in range(2,21):
    for i in range(1,11):
        print(num,"x",i, " = ",num * i,)
    print("\n")