even_odd = lambda num : "even" if num % 2== 0 else "odd"
print(even_odd(5))

sum = lambda a , b : a + b

print(sum(4,5))

table = lambda num , i : f"{num } * {i} = {num * i}"

for i in range(1,11):
    print(table(5,i))
    
calculator = lambda num1 , num2 , op :(
    num1 + num2 if op == "+" else
    num1 - num2 if op == "-" else
    num1 * num2 if op == "*" else
    num1 / num2 if op == "/" else
    num1 % num2 if op == "%" else
    "Invalid operator"
    )



print("Answer =", calculator(2, 5, "+"))