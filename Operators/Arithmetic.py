'''This file created to practice Arithmetic operator
Author - Sreeni added date:22/Feb/2024 '''

a = 15.0
b = 6
print("the value of a ", a)
print("the value of b ", b)

#Arithmetic Operators +,-,*, /, //, %,**

print("Addition of a & b ", a+b) # 21
print("Minus of a & b ", a-b) # 9
print("Mul of a and b", a*b) # 90   a & b multiplicants and a is multiplier
print("division of a/b", a/b) # 2.5 a is dividend and b is diviser, result is quotient, remainder
print("floor division of a//b ", a//b) # 2
print("Modulo of a and b", a%b) # 3
print(" a Power b", a**b) #

# String concatnation and multiplication
first_name = 'ETL'
lastname = "Automation"
d = 10
full_name = first_name + lastname + str(d)
print("full name", full_name) # addition both values should be in string form
source_count = 220
target_count = 218
mis_match = 2.3
a= 'Source count is'
b= 20
print( a + str(b))
print("Source count is " + str(source_count))
print("target count is ", target_count)
print("Mismatch per  is " + str(mis_match))

str = 'ETL'
str2 = 'AUtomation'
multiplier = 4

print("string multuplication", str * multiplier)
print('#########################################################')
print("#"*50)


#a+b*c/d

#BODMAS
#PEMDAS rule

#(), exponential, (MUl, div,add, sub)

#PEMDAS rule

print((8+2)*3/2)  #(10)*3/2--> 30/2 -->15
print((8+2)/(2*3)) # 10/(2*3) --> 10/(6)
print((8+2)/2*3) # (10)/2*3 --> 5*3-->15
print((8+2)/3*2+3*2) # (10)/3*2+3*2 --> 3.3*2+3*2-->6.6+3*2-->6.6+6--.12.6



a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print("Value of (a + b) * c / d is ",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print("Value of ((a + b) * c) / d is ",  e)

e = (a + b) * (c / d)   # (30) * (15/5)
print("Value of (a + b) * (c / d) is ",  e)

e = a + (b * c) / d      #  20 + (150/5)
print("Value of a + (b * c) / d is ",  e)



