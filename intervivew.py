# # reverse a string 
# text = "python"
# print(text[::-1])

# reverse = ""

# for ch in text:
#     reverse = ch + reverse
    
# print(reverse)
# # o(n)

# # palindrom

# if text == text[::-1]:
#     print("palindrom")
# else:
#     print("not pelindrom")
    
# #count vovel

# def count_vovel(text):
#     count = 0
#     for ch in text:
#         if ch in "aeiou":
#             count += 1
            
#     print(f"total vovels = {count}")
    
# count_vovel("python is easy language")


# def max_num(num1,num2,num3):
#     if num1 > num2:
#         if num1 > num3:
#             print(f"Max num = {num1}")
#         else:
#             print(f"Max num = {num3}")
#     else:
#         if num2 > num1:
#             print(f"Max num = {num2}")
#         else:
#             print(f"Max num = {num1}")
            
# max_num(35,34,56)


# def max_num2(num1,num2,num3):
#     if num1 > num2 and num1 > num3:
#         print(f"Maximum num is = {num1}")
#     elif num2 > num1 and num2 > num3:
#         print(f"Maximum num is = {num2}")
#     else:
#         print(f"Maximum num is = {num3}")
        
# max_num2(34,45,10)


# # prime  number


# def prime(num):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 print("Not prime = ",num)
#                 break
#         else:
#             print("prime = ",num)
            
#     else:
#         print(f"Not prime = {num}")
        
# prime(2)

# # remove duplicate

# def remove_duplicates(list):
#     unique = set()
#     duplicate = set()
    
#     for elem in list:
#         if elem in unique:
#             duplicate.add(elem)
#         else:
#             unique.add(elem)
            
#     print(f"duplicate elements = {duplicate}")
#     print(f"unique elements = {unique}")
    
# numbers = [1,2,2,3,4,5,5]
# remove_duplicates(numbers)


# # class 

# class Animal:
    
#     def sound(self):
#         print("animale make a sound")
        
# class Dog(Animal):
    
#     def bark(self):
#         print("bark")
        
# dog = Dog() 
# dog.sound()
# dog.bark()



# # polymorphizam

# class Dog:

#     def sound(self):
#         print("Woof")


# class Cat:

#     def sound(self):
#         print("Meow")


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()



# # Encapsulation

# class Student:
    
#     def __init__(self):
#         self.__marks = 90
        
#     def show_marks(self):
#         print(self.__marks)
        
# s = Student()
# s.show_marks()



list = [12,34,56,78,36]

largest = list[0]

for num in list:
    if num > largest:
        largest = num
        
print(largest)


list = [12,23,12,45,45,12,46,67]

unique = set()
duplicate = set()

for num in list:
    if num in unique:
        duplicate.add(num)
    else:
        unique.add(num)
        
unique -= duplicate
        
print(f"duplicates = {duplicate}")
print(f"unique = {unique}")

        