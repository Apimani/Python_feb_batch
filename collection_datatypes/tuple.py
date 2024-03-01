'''This file is created to practice tuple DT
Author - Sreeni added date:19/Feb/2024'''

#ls = [] # syntax to create list

tu = () # syntax to create tuple

print(type(tu))

tuple1 = (1,2,'ETL','Automation',10.5,1+2j, True)

print(tuple1)
print(type(tuple1))
# Accessing elements from list
print("tuple1[0]", tuple1[0])
print("tuple1[0]", tuple1[5])

ls = [1,2,3]
print("functions/Methods available in tuple", dir(tuple1))
print("functions/Methods available in list", dir(ls))

print("tuple.count(2)",tuple1.count(2))
print("tuple.index('Automation')",tuple1.index('Automation'))


print("tuple1[3]",tuple1[3])


# maps = (lat, lng)
# temp = [29, 32, 35, .....,]
