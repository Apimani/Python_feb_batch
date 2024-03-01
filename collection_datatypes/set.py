
s = {1,2,3}
print("The s and type of s",s, type(s))

s1 = {}
print("The s1 and type of s1",s1, type(s1))

s2 = set()
print("The s2 and type of s2",s2, type(s2))

print("methods vailable", dir(s))

s3 = {3,1,5,1,6,9,11,2,2,7,7,15,12,'test', False}


print("s3", s3)

s3.add(1000)

print("s3", s3)

s3.pop()
print("s3", s3)

#print(s3[0])

fs = frozenset(s3)
print("Methods available", dir(fs))
print("methods vailable", dir(s))
print(type(fs))

