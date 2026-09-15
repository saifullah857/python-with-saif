class Student:
    # class attr => hr aik object k liay same
    course = "python"
    timing = "10 - 12"
    course_duration = "3 months" 
    clg = "xyz"
    # class methods => specific object k liay hoty hai 
    def __init__(self ,name , fee ):
        self.name = name
        self.fee = fee    
    def intro(self):
        print(f"student name = {self.name} | fee = {self.fee} | course = {self.course}" )
        
    def fee_discount(self , discount):
        self.fee = self.fee - ( self.fee * discount/100)
        print(f"After discount fee = {self.fee}")
        
    
    
std1 = Student("Mustafa" , 5_000 )
std1.intro()
std1.fee_discount(5)

std2 = Student("Asad" , 3000)
std2.intro()
std2.fee_discount(7)

