# # # word = "AI ,is ,future"
# # # word2 = "is demanding skill"

# # # # print(len(word))
# # # # print(word + " " + word2)

# # # # print(word[2])
# # # # for i in word:
# # # #     print(i)
# # # # print(word[0:10])
# # # # print(word[5:10])
# # # # print(word[11:])

# # # # reverse a string
# # # # print(word[::-1])

# # # # print(word.lower())
# # # # print(word.upper())

# # # # print(word.title())
# # # # string = "artificial inteligence"
# # # # print(word.replace("AI", string).title())

# # # # print(word.split(","))

# # # # languages = ["Python", "Java", "C++"]
# # # # new_lang = "_".join(languages)
# # # # print(new_lang)

# # # # text = "   Python   "

# # # # print(text.strip())

# # # # print(word.count("A"))

# # # file1 =["python.py","javascript.py","index.html","style.cs"] 
# # # count = 0
# # # html_count = 0
# # # for file in file1:
# # #     if file.endswith("py"):
# # #         count += 1
# # #     elif file.endswith("html"):
# # #         html_count += 1
# # # print(f"only {count} py file exisit and {html_count} html file")




# # # print("Pakistan zindabad")
# # # print("Pakistan zindabad")
# # # print("Pakistan zindabad")
# # # print("Pakistan zindabad")
# # # print("Pakistan zindabad")



# # counter = 1
# # while counter <= 5: # 1 <= 5 | 2 <= 5 | 3 <= 5 | 4 <= 5 | 5 <= 5
# #     print("pakistan zindabad")
# #     counter = counter + 1 # count 
   
# # print("outside loop")









# # num = -34


# # if num > 0: # 12 > 0 
# #     print("+ve")
    
# # elif num < 0:
# #     print("-ve")
    
# # else:
# #     print("0")



# str = "madam"

# reverse = ""

# for chr in str:
#     reverse = chr + reverse

# if reverse == str:
#     print("palindrop")
# else:
#     print("Not palindrop") 



    
# numbers=[1,2,3,2,4,5,1]

# seen = set()

# duplicate = set()

# for num in numbers:
#     if num in seen:
#         duplicate.add(num)
#     else:
#         seen.add(num)
        
# print(duplicate)


# text="AI AI ML Python AI ML"

# words=text.split()

# print(words)


# for chr in text:
    
    
    
# text = "this is python with string . and i love doing code in python . its easy ."
# splited_text = text.split(" ")
# print(splited_text)



# # join string

# word1 = "python"
# word2 = "is"
# word3 = "amazing"

# combined_string = " ".join((word1,word2,word3))
# print(combined_string)


# roadmap1 = "python"
# roadmap2 = "ML"
# roadmap3 = "DL"
# roadmap4 = "Gen AI"
# roadmap5 = "Agentic AI"

# road_map = " -> ".join((roadmap1,roadmap2,roadmap3,roadmap4,roadmap5))
# print(road_map)



# text = "I love Python"

# print(text.find("love"))
    
    
# text = "Python"

# print(text.find("Java")) # not find then return -1

            
# text = "banana"

# print(text.find("a", 2, 5)) # find , start , end 



# text = input("Enter a sentence: ")
# word = input("Enter a word to find: ")

# position = text.find(word)

# print("Position:", position)



# count 
text = "banana"

print(text.count("a"))



# start with

filename = "report.pdf"

if filename.startswith("report"):
    print("This is the report file.")
    
    
    
# end with

# text = input("Enter a filename: ")

# if text.endswith(".pdf"):
#     print("This is a PDF file.")
# else:
#     print("This is not a PDF file.")









def sum(num):
    sum = 0
    
    for i in range(num + 1):
        sum += i
        
    print(f"total sum at the num = {sum}")
    
sum(6)


