import pandas as pd

import re
def add(a,b):
    return a+b
#
print(add(4,5))
# lambda arguments: logic
mul_lam = lambda a,b,c : a*b*c

print(mul_lam(5,6,10))




df = pd.read_csv(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\Employee.csv")
columns = df.columns
print(columns)

upper_case = lambda col:col.upper().strip()

def con_cols(col):
    col = col.upper().strip()

print(upper_case(' Name    '))

data = ['Identifier ', 'Surname ', ' given_name ', 'birthmonth ', 'Salary', 'Dept']

upper_colums = list(map(lambda col:col.upper().strip(),data))

print(upper_colums)

filter = list(filter(lambda value: value>0, [1,2,3,4,-1,-2,-7]))
print(filter)

emails = ["user1@example.com", "invalid_email", "user3@example.com"]
valid_emails = list(filter(lambda email: '@' in email and '.' in email[email.find('@'):], emails))
print(valid_emails)  # Output: ['user1@example.com', 'user3@example.com']

from functools import reduce

reduce = reduce(lambda a,b: a+b, [1,2,3,4,19,230,23])
print(reduce)




emails = ["user1@example.com", "invalid_email", "user3@example.com"]
valid_emails = list(filter(lambda email: '@' in email and '.' in email[email.find('@'):], emails))
print(valid_emails)  # Output: ['user1@example.com', 'user3@example.com']


