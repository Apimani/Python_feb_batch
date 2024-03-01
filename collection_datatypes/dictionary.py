'''This file created to practice Dictionary DT
Author - Sreeni added date:21/Feb/2024 '''

d = {}
print("type(d)",type(d))

d2 = {1,2,3}
print("type(d)",type(d2))

# list = [1,2,3], tuple = (1,2,3),set = {1,2,3}, frozenset = forozenset({12,34}) --> for all these types we only provided heterogenous elements
#     for all the above types keys will be indexes( Index will start from 0)
#d3 = {key:value, key2:value2, key3:value3}
d3 = {1:'sreeni', 2: 'Rahul', 3 : 'Pooja', 4 : 'Hari'}


# Access elements using key value and using get method
print("dictionary d3", d3)
print("d3[1]",d3[1])
print("d3[2]",d3[2])
print("d3[3]",d3[3])
print("d3[4]",d3[4])
print("access element by using get method d3.get(1)", d3.get(1))
print("access element by using get method d3.get(4)", d3.get(4))
#print("d3[1:5]",d3[1])
print("Methods available in dictionary", dir(d3))
# print all keys and values

print("Keys available in d3 ", d3.keys())
print("values available in d3 ", d3.values())
print(" type of Keys ", type(d3.keys()))
print(" type of values ", type(d3.values()))
print("key and values in d3", d3.items())

#update will be used to update existing key value and to insert new key-value pair

print("before update", d3)
d3.update({3:'Teja'})
print("after update", d3)
d3.update({3:'Ramesh', 4:'pooja', 5:'john'})
print("after second update", d3)
d3[1]='balaji'
d3[6]='Chandana'
print("after third update", d3)
d1 = {8:'etl', 9 : 'testing'}
d3.update(d1)
print("after fourth update", d3)

# delete the keys from dict
print("before delete d3",d3)
d3.pop(1)
print("after delete d3",d3)
d3.popitem()
print("after popitem delete d3",d3)
d3.popitem()
print("after popitem delete d3",d3)
del d3[2]
print("after del d3",d3)


d3 = {1:'sreeni', 2: 'Rahul', 3 : 'Pooja', 4 : 'Hari'}
d4 = {"fruits":["Mango","apple",''], "vegetables":["Tomoto", "onion","brinjal"]}


print("value of fruits",d4.get("fruits"))
print("value of fruits",d4["fruits"])

print('value of vegetables d4.get("vegetables")',d4.get("vegetables") )
print('value of vegetables d4.get("vegetables")[0]',d4.get("vegetables")[0])
print('value of vegetables d4.get("vegetables")[1]',d4.get("vegetables")[1])
print('value of vegetables d4.get("vegetables")[2]',d4.get("vegetables")[2])

print('value of fruits d4.get("fruits")',d4.get("fruits") )
print('value of fruits d4.get("fruits")[0]',d4.get("fruits")[0])
print('value of fruits d4.get("fruits")[1]',d4.get("fruits")[1])
print('value of fruits d4.get("fruits")[2]',d4.get("fruits")[2])



























# d2 = {1:"Sreeni",2:"Ramesh", 3:"Rahul"}
# print("type(d2)",type(d2))
#
# print("Data inside d dict",d)
# print("Data inside d2 dict",d2)
#
# print(dir(d2))
#
# # Keys and values
# print("Key available in d2 ", d2.keys())
# print("values available in d2 ", d2.values())
# print("Keys and values available in d2 ", d2.items())
#
# d2 = {1:"sreeni", 2:"ramesh", 1:"Ram", 3:"ramesh"}
# print(" Dictionary d2 values", d2)
#
# # Adding new values and update existing values
# d3 = { 1:"ramesh", 2:"Ram", 3:"ramesh"}
# print("Before adding key 4 to d3", d3)
# d3[4] = 'Ind'
# d3[2] = 'Ramnath'
# print("After adding key 4 to d3", d3)
#
# # Adding new values and update existing values using update
#
# print("Before adding key 5 to d3", d3)
# d3.update({5:"Somesh"})
# d3.update({3:"Upendra"})
# print("After adding key 5 to d3", d3)
#
# # Accessing the values from the dictionary
# print("dictionary d3", d3)
# print("d3.get(5)", d3.get(5))
# print("d3.get(4)", d3.get(4))
#
# print("d3[2]", d3[2])
# #print("d3[10]", d3[10])
#
# #remove the elements from dictionary
# print("before pop dictionary d3", d3)
# print("d3.pop(1)", d3.pop(1))
# print(" after pop dictionary d3", d3)
#
#
# #remove the elements from dictionary
# print("before popitem dictionary d3", d3)
# print("d3.popitem", d3.popitem())
# print(" after popitem dictionary d3", d3)
#
# d4 = {"fruits":["Mango","apple","guava"], "vegetables":["Tomoto", "onion","brinjal"]}
#
# print("fruits data",d4.get(1))
# #print("fruits data",d4[1])
# print("Type of fruits data",type(d4.get("fruits")))
# # print("before pop d4", d4)
# # d4.pop("fruits")
# # print(" after pop d4",d4)
#
# import pandas as pd
# df = pd.DataFrame(d4)
# print(df)
#
#
#
# #
#
#
#
#
#
# # Adding new values and update existing values
# d3 = { 1:"ramesh", 2:"Ram", 3:"ramesh"}
# print("Before adding key 4 to d3", d3)
# d3[4] = 'Ind'
# d3[2] = 'Ramnath'
# print("After adding key 4 to d3", d3)
#
# # Adding new values and update existing values using update
#
# print("Before adding key 5 to d3", d3)
# d3.update({5:"Somesh"})
# d3.update({3:"Upendra"})
# print("After adding key 5 to d3", d3)
#
# # Accessing the values from the dictionary
# print("dictionary d3", d3)
# print("d3.get(5)", d3.get(5))
# print("d3.get(4)", d3.get(4))
#
# print("d3[2]", d3[2])
# #print("d3[10]", d3[10])
#
# #remove the elements from dictionary
# print("before pop dictionary d3", d3)
# print("d3.pop(1)", d3.pop(1))
# print(" after pop dictionary d3", d3)
#
#
# #remove the elements from dictionary
# print("before popitem dictionary d3", d3)
# print("d3.popitem", d3.popitem())
# print(" after popitem dictionary d3", d3)
#
# d4 = {"fruits":["Mango","apple","guava"], "vegetables":["Tomoto", "onion","brinjal"]}
#
# print("fruits data",d4.get(1))
# #print("fruits data",d4[1])
# print("Type of fruits data",type(d4.get("fruits")))
# # print("before pop d4", d4)
# # d4.pop("fruits")
# # print(" after pop d4",d4)
#
# # import pandas as pd
# # df = pd.DataFrame(d4)
# # print(df)
# #
# # #New line from sreeni
#


