"""
string.py file is created to practise string datatype
version1 - created by : Sreeni on 13/02/2024
"""

name = 'Sreeni'
print("The value of name is", name)
print("Type of name is", type(name))
print("Memory address of name is", id(name))

name2 = '1234'
print("The value of name2 is", name2)
print("Type of name2 is", type(name2))
print("Memory address2 of name is", id(name2))

name3 = 'Sreeni 1234'
print("The value of name3 is", name3)
print("Type of name3 is", type(name3))
print("Memory address of name3 is", id(name3))

name4 = "Sreeni 1234"
print("The value of name4 is", name4)
print("Type of name4 is", type(name4))
print("Memory address of name4 is", id(name4))

name5 = """Sreeni 1234"""
print("The value of name5 is", name5)
print("Type of name5 is", type(name5))
print("Memory address of name5 is", id(name5))

name6 = '''Sreeni 1234'''
print("The value of name6 is", name6)
print("Type of name6 is", type(name6))
print("Memory address of name6 is", id(name6))

str1 = "O'neil"
str2 = "I don't know"

print("The value of str1 is", str1)
print("Type of str1 is", type(str1))
print("Memory address of str1 is", id(str1))

print("The value of str2 is", str2)
print("Type of str2 is", type(str2))
print("Memory address of str2 is", id(str2))

str3 = 'O"neil'
str4 = 'I don"t know'

print("The value of str3 is", str3)
print("Type of str3 is", type(str3))
print("Memory address of str3 is", id(str3))

print("The value of str4 is", str4)
print("Type of str4 is", type(str4))
print("Memory address of str4 is", id(str4))


str5 = """ Python is a high-level, ' general-purpose programming language, 
          Its design philosophy 
          emphasizes code "readability with 
          the use of significant indentation. """


print("The value of str5 is", str5)
print("Type of str5 is", type(str5))
print("Memory address of str5 is", id(str5))

str6 = ''' Python is a high-level, ' general-purpose programming language, 
          Its design philosophy 
          emphasizes code "readability with    
          the use of significant indentation. '''

print("The value of str6 is", str6)
print("Type of str6 is", type(str6))
print("Memory address of str6 is", id(str6))

query = " select * from table where firt_name = 'sreeni' and last_namae like '%KA%' "

print("The value of query is", query)

query2 = """ select * from emp a inner join dept b
          on a.empno = b.empno 
          where a.firt_name = 'sreeni' """

query3 = ''' select * from emp a inner join dept b
          on a.empno=b.empno 
          where a.firt_name = 'sreeni' '''


str7 = 'sreenI232 '

print("methods available in string datatype",dir(str7))

print("Before capitalize str7 is ", str7)
print("After capitalize str7 is", str7.capitalize())

print("Before casefold str7 is ", str7)
print("After casefold str7 is", str7.casefold())

print("Before lower str7 is ", str7)
print("After lower str7 is", str7.lower())

query3 = ''' select * from emp a inner join dept b
          on a.empno=b.empno 
          where a.firt_name = 'sreeni' '''

print, type, id


query3 = query3.center(200)
txt = "banana"
x = txt.center(10)
print(x)
str8 = 'Sreenivas'
print(f"count of e in {str8}", str8.count('a'))

print("*"*50)

str = "Automation Testing"

print("str.startswith('Auto')",str.startswith('Auto'))
print("str.startswith('auto')",str.startswith('auto'))
print("Ends with Testing ",str.endswith('Testing'))
print("str.endswith('testing')",str.endswith('testing'))

print("str.find('Test')",str.find('Test'))

print("str.find('i')",str.find('i'))

print("str.find('i',8)",str.find('i',8))

print("str.find('i',8,12)",str.find('i',8,12))

name = 'Hari'
age = 24

print("My name is {name} and age is {age}".format(name=name,age= age))
name = 'Sreeni'
age = 25
print(f"My name is {name} and age is {age}")

env = ['dev', 'qa']
table = ['emp', 'dept']
for i in env:
    for j in table:
    #print(i)
        print(f"select * from {i}.{j}")

str = 'ETLbatch3'

print(f"str.isalnum() on {str}", str.isalnum())
str2 = 'ETL_batch3'
print(f"str2.isalnum() on {str2}", str2.isalnum())

str3 = 'ETLbatch'
print(f"str3.isalnum() on {str3}", str3.isalpha())

str4 = 'ETLbatch1'
print(f"str4.isalnum() on {str4}", str4.isalpha())

str = ' Sreeni Kattu  '
print("length of str before strip", len(str))
print(f"str.strip()", str.strip())
print("length of str after strip", len(str.strip()))

print(f"str.rstrip()", str.lstrip())
print("length of str after lstrip", len(str.lstrip()))
print(f"str.lstrip()", str.lstrip())
print("length of str after rstrip", len(str.rstrip()))
str7 = 'ETL Automation'
print(f"str7.lstrip()", str7.rstrip('Automation'))
str8 = 'ETL Automation'
print(f"str8.lstrip()", str8.lstrip('ETL'))

str9 = 'ETL-Bigdata-testing-automation'
str10 = 'ETL,Bigdata,testing,automation'

print('str9.split("-",2)',str9.split("-"))
print('str10.split(",",2)',str10.split(","))
print('type str10.split(",",2)',type(str10.split(",")))












