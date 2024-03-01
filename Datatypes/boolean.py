"""
docs strings : helps user to understand all about this file
int.py file is created to practise boolean datatype
version1 - created by : Sreeni on 15/02/2024
"""

a = True
b = False


print("Value of a is ", a)
print("Type  of a is ", type(a))
print("Memory location  of a is ", id(a))

print("Value of b is ", b)
print("Type  of b is ", type(b))
print("Memory location  of b is ", id(b))

c = True

print("Value of c is ", c)
print("Type  of c is ", type(c))
print("Memory location  of c is ", id(c))

is_married = True # yes/No
is_approved = False
#Current_address_ind = True

print("Methods available in boolean type", dir(True))

print("c.real", c.real) # True = 1+0j
print("b.real", b.real) # false = 0+0j

d = True
e = True
f= False
print("d.__add__(e)",d.__add__(e))
print("d.__add__(f)",d.__add__(f))

print("c.imag", c.imag)
print("b.imag", b.imag)

#complex = 1 + 2j

complex = -1 + 2j

print("Value of complex is ", complex)
print("Type  of complex is ", type(complex))
print("Memory location  of a is ", id(complex))

print(" real of complex is ", complex.real)
print("Imaginary  of complex is ", complex.imag)
print("Methods available in complex type", dir(complex))


