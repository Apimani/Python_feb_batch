"""
docs strings : helps user to understand all about this file
int.py file is created to practise integer datatype
version1 - created by : Sreeni on 13/02/2024
"""

count = 10

print("The value of count is", count)
print("Type of count is", type(count))
print("Memory address of count is", id(count))

count2 = 10

print("The value of count2 is", count2)
print("Type of count2 is", type(count2))
print("Memory address of count2 is", id(count2))

count3 = 15

print("The value of count3 is", count3)
print("Type of count3 is", type(count3))
print("Memory address of count3 is", id(count3))

count4 = 10

print("The value of count4 is", count4)
print("Type of count4 is", type(count4))
print("Memory address of count4 is", id(count4))

count5 = 15

print("The value of count5 is", count5)
print("Type of count5 is", type(count5))
print("Memory address of count5 is", id(count5))

count6= -15

print("The value of count6 is", count6)
print("Type of count6 is", type(count6))
print("Memory address of count6 is", id(count6))

print("absolute number", count6.__abs__())
print("add two numbers count5 and count6 number", count6.__add__(count5))

print("functions available in integer type",dir(1))

print(help(count6.__add__))



