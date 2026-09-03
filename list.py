countries = ['pakistan','india','bangladesh','india','iran','chaina','USA']

# print(countries[2:4])
# print(countries[2:])
# print(countries[:5])
# print(countries[-5:-2])
# print(countries[::-1])



# for country in countries:
#     if country == "pakistan":
#         print("yes in list")

countries.append("israell")
countries.insert(2,"uk")
countries.pop(1)
countries.extend(["palasteen"])
countries.remove('india')
countries.clear()
print(countries)
