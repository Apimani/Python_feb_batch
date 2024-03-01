ls = [1,2,3]
print("the values of ls", ls)
print("The location of ls ", id(ls))

ls.append(5)

print("after append")

print("the values of ls", ls)
print("The location of ls ", id(ls))

ls.append(100)
ls.pop(3)

print("after append 100 and pop index 3")

print("the values of ls", ls)
print("The location of ls ", id(ls))

ls = [1,2,3,4,5,1,2,22,22,2,]#--> 0:1, 1:2...
print(ls)

tu = (1,2,3,4,5,5,5,5,5)

tu.append(2)

print(tu)