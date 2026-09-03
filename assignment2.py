# Q3. Write a function that prints the digits of a number, . 
# For eg:n = 321 , there are 3 digits in it 3, 1 and 2 & we need to print them. 

# [Hint - The right most digit of a number N is N%10. 
# And to remove the right most digit from a number, we can do N = N / 10.] 


# def print_seperate_digit(num):
#     print(f"Before seperation num = {num}")
#     length = len(str(num))
#     for i in range(length):
#         last_part = num % 10 
#         print(last_part)
#         num = num // 10
        
# print_seperate_digit(4535)




# def count_num(num): # 456
#     count = 0
#     while num > 0:
#         count += 1 
#         num = num // 10 
        
#     return count




def check_num():
    while True:
        num = input("Enter any num  or quite = ")
        
        if num == "quite":
            break
        else:
            num = int(num)
            
            if num > 0:
                print(f"positive num = {num}")
            elif num < 0:
                print(f"-ve num = {num}")
            else:
                print("0")
                
        

# check_num()




def gessing_game():
    seceret = 30
    count = 0
    while True:
        num = int(input("Enter a num = "))
        if num == seceret:
            print("You win")
            count += 1
            break
        else:
            if num > seceret:
                print("Too High")
                count += 1
            else :
                print("Too low")
                count += 1
    print(f"you win in attempts = {count}")
    
    
# gessing_game()




def prime(start,end):
    count = 0
    prime = []
    for num in range(start,end + 1):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                count += 1
                prime.append(num)    
    print(f"count of prime between range {start} - {end} = {count}")
    print(f"All prime num = {prime}")

prime(10,50)

