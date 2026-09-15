# # file operations 

# # 1 - open a file => use open(path , mode) fnx

# f = open("data.txt" , "r") # f contain all information of that file
# # data = f.read()
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# print(type(data))


# # 2 - write operation 
# f = open("data.txt" , "w") # for write operation it is necessary to open file in write mode
# f.write("Text to overwrite \n the complete data. write operation sy hamaraa \n pehly wala data delete ho jata hai \n aur jo text hum ny write operation \n mein likha hota hai wo overwrite ho jata hai")


# f.close() # we will always close the file when we open it => to prevent it from unexpected changes

# # - - - - - - - - - - - - - -  - - - - - - - - - - -  - - -  -

# # Modes in File operations
# # 1 - r => reading(defalut mode)
# f = open("data.txt")
# print(f.read())
# # 2 - w => writing , truncate file first
# f = open("data.txt" , "w")
# f.write("new text will replace the old text")
# # 3 - x => creates new & open for writing => it is used when we wants to dedicatily create new file 
# # concept => w , and x can create file so which is the basic diffrence between them
# # if file exist w => truncate file and overwrite txt
# # but x through an error so we prevent file from unexpected changes
# # f = open("sample.txt" , "x")
# f.write("this is a sample file created by using a x mode in file i / o")
# # 4 - a => writing , appends at end
# f = open("data.txt" , "a")
# f.write(" \n this text not truncate the existing text rather \nit add at the end of existing text")
# # 5 - b => binary mode => to store data in diff formats like => audio , video etc
# # 6 - t => text mode (defalut)
# # 7 - + => open disk file for update( r & w ) => can use for multiple modes => eg r+(read & write) , w+(write & read) , a+(append & read)
# # what is basic diff when all perform same task => read & write =>
# # r+ => pointer available at frst idx => wants to perform read and write from start => r+
# # a+ pointer start from end we start writing from the end of file
# # w+ truncate file and start reading from start


# # r+

# f = open("sample.txt", "r+") # it overwriten existing text with new at the start
# f.write("123")
# print(f.read())

# # a+

# f = open("sample.txt", "a+") #not show anyhing in print bcz our pointer at the end of file 
# f.write("123")
# print(f.read())

# # w+
# f = open("sample.txt", "w+") #not show anyhing in print bcz our pointer at the end of file aftr wrting task perform
# f.write("123")
# print(f.read())


# f.close()

# # - - - - -  - -  -  - - - - - - - - - - - - - - - - - - - - - -- -  - ---- - - -  

# # with keyword => we dont have to need to clodse our file 

# with open("data.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(len(data))
    
    
# # delete a file 

# import os 

# os.remove("sample.txt")


# # activity to search in file => truncate 




word = "truncate"
line = 0
with open("data.txt" , "r") as f:
    while True:
        data = f.readline()
        line += 1
        if word in data:
            print(f"{word} found at line {line}")
            break
        