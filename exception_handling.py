
# exception handling => error => complete stuck=> exception handling
# error =>
# except => error through => msg show 
try:
    x = int(input("Enter value of x : "))
    ans = 10 / x
    
except ZeroDivisionError: # python predefined error
    print(f"divide by zero is not allowed")
    
except ValueError:
    print("Invalid input entered")
    
else:
    print(f"ans = {ans}")
    print("Program runs without invalid inputs")
    
finally:
    print("End of program")
    
    x = input("Enter your name = ")
    print("your name = ", x)
    