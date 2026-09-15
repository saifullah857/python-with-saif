line = 1
word = "truncate"
with open("data.txt" , "r") as f:
    while True:
        data = f.readline()
        if (word in data):
            print(f"{word} found at line =" , line)
            break
        print(data)
        line += 1