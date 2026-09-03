nums = {1,2,3,4,5,6,7,8,9,10}
print(nums)
print(type(nums))
print(len(nums))

even = set()

for num in nums:
    if num % 2 == 0:
        even.add(num)


print(even)

nums.add(100)
nums.discard(99)
nums.pop() # random value ko remove krny k liay 
print(nums)



# uninion
num1 = {1,2,3,4,5 ,7 ,0}
num2 = {6,7,8,9,0}

result = num1.union(num2)

print(result)


# intersection

result = num1.intersection(num2)
print(result)


# diffrence
num1 = {1,2,3,4,5 ,7 ,0}
num2 = {6,7,8,9,0}


result = num2.symmetric_difference(num1)
print(result)


num1 = {1,2,3,4,5,6,7,8,9}
num2 = {5,6,7}

print(num1.issuperset(num2))