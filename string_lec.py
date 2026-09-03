# word = "Artificial Inteligence"
# word01 = "using python"
# word02 = "using js"
# word03 = "using jawa"

# result = word + " " +  word01 + " " + word02
# print(result)

# # indexing => specific part ko extract krna 

# print(word[4])
# print(word01[5])

# # immutable => changes are not allowed

# # word[0] = "a"
# print(word)

# # string iterateable 
# count_i = 0
# for chr in word:
#     if chr.lower() == "i":
#         count_i += 1
# print(count_i)





# # Indexing in python => accesing specific chr in sting

s = "python"

# print(s[1])
# print(s[4])
# print(s[-2])


# slicing => cut the string

# last is not included

print(s[1:5]) # start , end , step 
print(s[:5]) # start , end , step 
print(s[1:]) # start , end , step 
print(s[:]) # start , end , step 


# negitive slicing

print(s[-4:-1])
print(s[::-1])


s = "madamm"
if s[::-1] == s:
    print(f"your string {s} is plaindrop")









    


