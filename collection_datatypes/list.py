'''This file is created to practice list DT
Author - Sreeni added date:19/Feb/2024'''

a = 120
f = 10.20
s = 'etl'

# ls = [1, 1.06,'ETL', 1+2j,True, 34, 340]
# print(type(ls))

ls = [1,2,3,'ETL','Automation',10.5,1+2j, True]

print(ls)
print(type(ls))
# Accessing elements from list
print("ls[0]", ls[0])
print("ls[1]", ls[1])
print("ls[2]", ls[2])
print("ls[3]", ls[3])
print("ls[4]", ls[4])
print("ls[5]", ls[5])
print("ls[6]", ls[6])
print("ls[7]", ls[7])
#print("ls[8]", ls[8])

# checking type of elements available inside the list
print("Type of ls[0]", ls[0], type(ls[0]))
print("Type of ls[3]", ls[3], type(ls[3]))
print("Type of ls[5]", ls[5], type(ls[5]))
print("Type of ls[6]", ls[6], type(ls[6]))
print("Type of ls[7]", ls[7], type(ls[7]))
print("Methods available in list",dir(ls))

# Append , Extend
ls = [1,2,3]
print("list before append" , ls)
ls.append(4)
print(" list after append 4", ls)
ls.append(5)
print(" list after append 5", ls)
ls.append([5,6,7])
print(" list after append [5,6,7]", ls)
ls.append(8)
print(" list after append 8", ls)

ls.append('etl automation')
print(" list after append 8", ls)

ls.append((1,2,3))
print(" list after append (1,2,3)", ls)
ls.extend([10,11,12]) # extend will take each value from iterable type and append to end of list
print("list aftetr extend [10,11,12]", ls)
ls.extend([23]) # extend method takes iterable items like list, tuple, set, frozen set, etc
print("list aftetr extend [23]", ls)
print( '*' *40)
print(ls)

# count


ls = [1,2,3,4,1,1,1,5,5,2]
print("count of 1", ls.count(1))
print("count of 5", ls.count(5))
print("count of 5", ls.count(10))

# Index

ls = [1,'sreeni','auto','etl','auto']
print("ls.index('auto')", ls.index('auto'))
print("ls.index('auto')", ls.index('etl'))
#print("ls.index('auto')", ls.index('kat'))

# insert
print("list before insert", ls)
ls.insert(0,'kat')
print("list after insert", ls)
ls.insert(5,'hari')
print("list after insert at 5", ls)
ls.insert(20,'wrong')
print("list after insert at 20", ls)
print("ls.index('wrong')", ls.index('wrong'))

# pop and remove and del

ls = [3,'etl','automation',1,2]

print("list before pop", ls)
ls.pop() # index based deletion
print("list after pop", ls)
ls.pop(2)
print("list after pop", ls)

ls = [3,'etl','automation',1,2, 'etl']
print("before remove", ls)
ls.remove('etl') # remove is value based deletion
print("list after remove", ls)

del ls[1] # index based deletion

print("list after del", ls)

ls = [1,4,1,6,8,10,2]

ls.sort(reverse=True)

print("after sort", ls)

ls = [1,2,3,4,7,5]

ls.reverse()

print(ls)



#coordinates = (40.7128, -74.0060)
