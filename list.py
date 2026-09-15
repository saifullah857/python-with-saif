# countries = ['pakistan','india','bangladesh','india','iran','chaina','USA']

# # print(countries[2:4])
# # print(countries[2:])
# # print(countries[:5])
# # print(countries[-5:-2])
# # print(countries[::-1])



# # for country in countries:
# #     if country == "pakistan":
# #         print("yes in list")

# countries.append("israell")
# countries.insert(2,"uk")
# countries.pop(1)
# countries.extend(["palasteen"])
# countries.remove('india')
# countries.clear()
# print(countries)

subjects = ["English" , "Math" , "Urdu" , "Islamiyat" , "Science"]
marks = [85 , 99 , 89 , 95 , 85]
obtained_marks = 0
total_marks = len(marks) * 100
print(f"{'='*5} Student Summery {'='*5}")
for idx , (subject , mark) in enumerate(zip(subjects , marks)):
    print(f"{idx + 1} - In  {subject} = {mark} marks")
    obtained_marks += mark    
percentage = obtained_marks / total_marks * 100
if percentage >=90:
    grade = "A+"
elif percentage >=80:
    grade = "A"
elif percentage >=70:
    grade = "B+"
elif percentage >= 60:
    grade = "C+"
elif percentage >= 50:
    grade = "D+"
else:
    grade = "F"    
print(f"Total marks = {total_marks}")
print(f"Obtained marks = {obtained_marks}")
print(f"percentage = {percentage}")
print(f"Student grade = {grade}")
    

    