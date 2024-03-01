# '''This file created to practice iterative statements
# Author - Sreeni added date:27/Feb/2024 '''
#
# #str = 'ETL Automation'
# ls = [4,5,6,'Sreeni', True]
# t = (44,55,77,'Raghav', False)
# # d = {1:"Sreeni", 2:"Raghav", 3 :"Mahesh"}
# s= {7,1,2,3,4,5,5,6,6}
# fs = frozenset({1,4,5,6,7,7,7,8})
# # r = range(1,10)
#
# ls = [4,5,6,'Sreeni', True]
# # print("ls[0]", ls[0])
# # print("ls[1]", ls[1])
# # print("ls[2]", ls[2])
# # print("ls[3]", ls[3])
# # print("ls[4]", ls[4])
#
# # print("index")
# # print(ls.index(5))
# #syntax
# #for iterator_name in iterative_datatype_data : stmts
#
# num=0
#
# for i in ls:
#     index_val= ls.index(i)
#     # print("index values", index_val)
#     print(f"ls[{index_val}]", i)
#
#
# for i in s:
#     print(i)
#
# for i in t:
#     index_val= t.index(i)
#     # print("index values", index_val)
#     print(f"t[{index_val}]", i)
#
# print("#"*50)
# d = {1:"Sreeni", 2:"Raghav", 3 :"Mahesh"}
#
# print("d.keys()", d.keys())
# print("d.values()", d.values())
# print("d.items()", d.items())
#
# for key in d.keys():
#     print(key)
#
# for value in d.values():
#     print(value)
#
# for key, value in d.items():
#     print(f"Key is {key} and value is {value}")
#
# str = 'ETL Automation'
#
# print("str[0]", str[0])
# print("str[1]", str[1])
# print("str[2]", str[2])
#
#
# print("#"*50)
# for i in str:
#     #print(i)
#     if i.lower() in ['a', 'e', 'i','o','u']:
#         print("This is vowel",i)
# #     else:
#         print("This is not vowel", i)
#
#
# print("Nested foor loops")
#
# #syntax : range(start, end, step) # start and step optional and end is mandatory
#
# range(10) # range(0,10,1)
#
# print("type of range(10)", type(range(10)) )
#
# print("values of range(10)", range(10))
#
# for i in range(10): # range(0,9,1)
#     print(i)
# print("#"*50)
#
#
# for i in range(10,2,-1): # range(10,2,1)
#     print(i)
#
# print('#'*50)
#
# for i in range(10,0,-1):
#     print(i)
#
# ls = [1,2,3,4,5,6,7,8,9,10]
#
#
# for i in ls:
#     if i % 2 == 0:
#         print(f"{i} is even number")
#     else:
#         print(f"{i} is odd number")
#
# print("*"*50)
# for i in range(1,11):
#     if i % 2 == 0:
#         print(f"{i} is even number")
#     else:
#         print(f"{i} is odd number")
#
# print("*"*50)
# for i in range(1,101):
#     if i % 2 == 0:
#         print(f"{i} is even number")
#     else:
#         print(f"{i} is odd number")
#
# print("*"*50)
# for i in range(-20,10):
#     if i>=0:
#         print(f"{i} is positive number")
#     else:
#         print(f"{i} is negitive number")
#
# print('#'*50)
#
# total=0
# for i in range(1,4): #1,2,3
#     print(f"i value in current iteration is", i)
#     for j in range(4,8): # 4,5,6,7
#         print("j value in current iteration is", j)
#         for k in range(8,10): # 8,9
#             print("k value in current iteration is", k)
#             total +=1
# print(total)

for i in range(1,20): # 1,2,3,4,5
    #print(f"i value in current iteration is", i)
    for j in range(1,21): # 1,2,3,4,5,6,7,8,9,10
        #print(f"i value in current iteration is", i)
        #print(f"j value in current iteration is", j)
        print(f"{i}*{j} =",i*j)













