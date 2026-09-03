# Normal -->   Procedural programing (fnx)  --> OOP (classes , objects)


# class Student:
#     course = "python"
#     college = "Abbas College of Technology"
#     duration = "3 monts"
#     fee = 5000
#     timing = "10:00 AM - 12:00 AM"


    
# marrayam = Student()
# marrayam_2 = Student()
# print(marrayam.course , marrayam.college , marrayam.duration , marrayam.fee)
# print(marrayam_2.course , marrayam_2.college , marrayam_2.duration , marrayam_2.fee)


# classes => Blue prints that store 2 things 

# 1 - Properties => Data , Variables
# 2 - Methods => fnx , procedures

# ----------------------------------------------------------------------------------------------

#### CONSTRUCTER IN PYTHON ###

# __init__ Method => object ko intilize krta hai => called everytime when we create object of class

# class Student:
#     def __init__(self): # it can be abc => it store current instance of class => refrence of current obj
#         print("Constructer was created")
        
# marrayam = Student()

# constructer with parameters 
# ---------------------------------------------------------------------------------------------
class Student:
    def __init__(self , name , course , duration , fee , timing):
        self.name = name
        self.course = course
        self.duration = duration
        self.fee = fee
        self.timing = timing
        
    def intro(self):
        print(f"Student name = {self.name} his / her course = {self.course} with duration = {self.duration} paying fee = {self.fee} and timing = {self.timing}")
        
# yaha pr jo b pass hoga wo self mein save hoga
std1 = Student("Marrayam" , "python" , "3 monts" , 5000, "10 - 12")
# print(std1.intro())

# --------------------------------------------------------------------------------------------
# Types of constructer
# 1- default => self
# 2 - parameterized construcer
# note only one constructer hona cheiay hr aik class k liay


# --------------------------------------------------------------------------------------------


# Attributes in class and objects 

# 1 - class attribute => attributes belong to class => common for all objects 

# class Student:
#     course = "python"
#     college = "Abbas College of Technology"
#     duration = "3 monts"
#     fee = 5000
#     

# 2 - instance attribute => attr belong to obj => unique for all obj
# note => by using class we can just acces class attr
# Example print(Student.course) # python but print(Student.name) gives error becaues we are accesing obj attr

# class Student:
#     def __init__(self , name , course , duration , fee , timing):
#         self.name = name
#         self.course = course
#         self.duration = duration
#         self.fee = fee
#         self.timing = timing
        
#     def intro(self):
#         print(f"Student name = {self.name} his / her course = {self.course} with duration = {self.duration} paying fee = {self.fee} and timing = {self.timing}")
        
# std1 = Student("Marrayam" , "python" , "3 monts" , 5000, "10 - 12")

# --------------------------------------------------------------------------------------------

# Methods in class 


# 1 - Instance => compalsary parameter (self) = => it can also access class attr | obj atrr
class Laptop:
    storage_type = "ssd" # class attr
    
    def __init__(self ,name , RAM , storage):
        self.name = name
        self.RAM = RAM
        self.storage = storage
    
    def intro(self): # instance method 
        print(f"Lapton = {self.name} | RAM = {self.RAM} | storage = {self.storage} | storage_type = {self.storage_type}")
        
l1 = Laptop("Lenovo" , "8GB" , "256")
l2 = Laptop("HP" , "16GB" , "256")

l2.intro()

# 2 -  class method => 1st parameter cls => they can only acces class attr not other like obj attr => also use the decorator by using @classmethod

# decorator => that take another fnx and return it after changing its behaviour

class Laptop:
    storage_type = "ssd" # class attr
    
    def __init__(self ,name , RAM , storage):
        self.name = name
        self.RAM = RAM
        self.storage = storage
    
    def intro(self): # instance method 
        print(f"Lapton = {self.name} | RAM = {self.RAM} | storage = {self.storage} | storage_type = {self.storage_type}")
        
    @classmethod # change the behaviour to make it class method   
    def get_storage_type(cls): # only can access class attr
        print(f"storage type = {cls.storage_type}")
        
l1 = Laptop("Lenovo" , "8GB" , "256")
l2 = Laptop("HP" , "16GB" , "256")

l1.get_storage_type()


# --------------------------------------------------------------------------------------------
# 3 - static method => no complosory parameter => no self | class parameter(noraly initialized) ==> no access to class as well as instance attr ==> use a decorator caleed @staticmethod ==> used to combine related logic of class

class Laptop:
    storage_type = "ssd" # class attr
    
    def __init__(self ,name , RAM , storage):
        self.name = name
        self.RAM = RAM
        self.storage = storage
    
    def intro(self): # instance method 
        print(f"Lapton = {self.name} | RAM = {self.RAM} | storage = {self.storage} | storage_type = {self.storage_type}")
        
    @classmethod # change the behaviour to make it class method   
    def get_storage_type(cls): # only can access class attr
        print(f"storage type = {cls.storage_type}")
        
    @staticmethod
    def discount(price , discount):
        final_price = price - (discount * price / 100)
        print(f"discounted price = {final_price}")
        
l1 = Laptop("Lenovo" , "8GB" , "256")
l2 = Laptop("HP" , "16GB" , "256")

# l2.discount(50000 , 20)



#--------------------------------------------------------------------------------------------

class Product:
    count = 0
    
    def __init__(self  , name , price):
        self.name = name
        self.price = price
        Product.count += 1
    
        
    def get_info(self):
        print(f"prodect name = {self.name} | price = {self.price}")
        
    @classmethod
    def get_count(cls):
        print(f"Total objects are ceated = {cls.count}")
        
    @staticmethod
    def discount(price , discount):
        print(f"discounted price = {price * discount / 100}")
        
    
p1 = Product("laptop" , 50_000)
p2 = Product("mobile" , 40_000)
p3 = Product("macbook" , 30_000)

print(Product.count)
p1.discount(p1.price , 12)


# Pillers of OOP
# 1 - Encapsulation => wrapping data & functions into a single unit
# note => data hiding perform krty hai 
# level of data 
# 1 - public data => inside class => accessible inside and outside the class
# 2 - protected attr => can acess inside class and subclass(inheritence)
# 3 - private => can only access inside the class
# note => it is not forceable that we cannot use protected outside the class

# note => to access private attr we use fnx getters and setters
class BankAccount:
    def __init__(self ,account_id , name , balance):
        self._account_id = account_id # underscore to make it protected
        self.name = name # public attr
        self .__balance = balance # double - underscore to make it private
    # getter => to get attr   
    def get_balance(self):
        return self.__balance
    # setter to set new attr
    def set_balance(self , newBalance):
            self.__balance = newBalance
        
acc1 = BankAccount(101 ,"Asad" , 100_000)
acc1.set_balance(200_000)
print(acc1._account_id ,acc1.name , acc1.get_balance())
# we can also access the private attr 
print(acc1._BankAccount__balance)

# 2 - Inheritence => Reusing attr & methods from parent (base) class to child class
# note => yaha pr hi hamara data hiding ka concept atta hai k kuch information ko hum child class sy protect krna chahty hai to hum private(no subclass access) | protected(access to subclass)
class Employee:
    start_time = "10 AM"
    end_time = "6 PM"
    
    def change_time(self , new_end_time ):
        self.end_time = new_end_time
    
class Teacher(Employee): # child class
    def __init__(self , subject):
        self.subject = subject
        
class AdminStaff(Employee):
    def __init__(self , role):
        self.role = role
        
t1 = Teacher("AI")
t1.change_time("5 PM")
print(t1.subject , t1.start_time , t1.end_time)

staff1 = AdminStaff("Directer")
staff1.change_time("3 PM")
print(staff1.role ,staff1.start_time,staff1.end_time )

# Types of inheritence 
# 1 - single level inheritence 
# 2 - Multilevel inheritence 


class Employee:
    start_time = "10 AM"
    end_time = "6 PM"
    
    def change_time(self , new_end_time ):
        self.end_time = new_end_time
        
class AdminStaff(Employee):
    def __init__(self , role):
        self.role = role
        
class Accountant(AdminStaff):
    def __init__(self, salary , role):
        super().__init__(role) # super keyword is used to call constructer of parentclass
        self.salary = salary
        
acc1 = Accountant(75_000 , "CA")
print(acc1.salary , acc1.role , acc1.start_time , acc1.end_time)
        
# 3 - Multiple inheritence 

class Teacher:
    def __init__(self , salary , subject):
        self.salary = salary
        self.subject = subject
        
class Student:
    def __init__(self , gpa , fee):
        self.gpa = gpa
        self.fee = fee

class Teacher_Assistent(Teacher , Student):
    def __init__(self, salary, subject , gpa ,fee , name):
        super().__init__(salary, subject)
        Student.__init__(self , gpa , fee)
        self.name = name
        
ta = Teacher_Assistent(45_000 , "AI" , 3.51 , 30_000 , "Saif")
print(ta.name , ta.salary , ta.subject , ta.gpa)

# Abstarction -> hiding internel details and showing only essential details
# data hiding define(public , protected , private ) | abbstraction mein hum decide krty hai k konsy data ko hum ny hide krna hai aur pls konsy data ko hum ny show krna hai 
# practical example query -> LLM -> output | konsa ml algorithm apply hua wo nhi pata 

# to implement abstarct class => blue print for other class => blue print kehny ka mtlb hai k enki khud ki instance ya attr nhi hoti but en sy hum dusri classes create krty hai => part of abc module => module means k aik code jo kiai or programmer ny likha hua hai jinko hum apni need k accordingly use krty hai => we have to just import and use it 

from abc import ABC , abstractclassmethod

class Animal(ABC): # make it abstarct class
    @abstractclassmethod
    def make_sound():
        pass # pass means we send null value | yani abhi hum koi kaam perform nhi krwa rhy hai
    
class Lion(Animal):
    def make_sound(self):
        print("ROARE!")  
        
class Cow(Animal):
    def make_sound(self):
        print("MAO!")  
        
lion = Lion()
lion.make_sound()

cow = Cow()
lion.make_sound()


# 2nd example 
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class JazzCash(Payment):

    def pay(self, amount):
        print(f"Processing JazzCash payment of Rs. {amount}")
        print("Payment successful through JazzCash!")


class EasyPaisa(Payment):

    def pay(self, amount):
        print(f"Processing EasyPaisa payment of Rs. {amount}")
        print("Payment successful through EasyPaisa!")


class Bank(Payment):

    def pay(self, amount):
        print(f"Processing Bank payment of Rs. {amount}")
        print("Payment successful through Bank!")


print("===== PAYMENT SYSTEM =====")

jazzcash = JazzCash()
jazzcash.pay(5000)

print()

easypaisa = EasyPaisa()
easypaisa.pay(3000)

print()

bank = Bank()
bank.pay(10000)


# 4 - Polymorphism => many forms => multiple fnx create with same name but it has diff operation
# ex = method overloading => + operator | add 2 nums | add 2 strings

# types of polymorphism
# 1 - fnx overriding (inheritence) | rededifinng parent class fnx in child lass


class Employee:
    def get_designation(self):
        print("Designation = Employee")
        
class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")
        
t1 = Teacher()
t1.get_designation()

# 2 - Duck typing => based on concept which is => walk like a duck



class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

class Robot:
    def speak(self):
        print("Beep Boop")

def make_it_speak(entity):
    entity.speak()   # type doesn't matter

for e in [Dog(), Cat(), Robot()]:
    make_it_speak(e)








