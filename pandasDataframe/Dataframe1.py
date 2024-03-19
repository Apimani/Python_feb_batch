import pandas as pd

ls = [1,3,4,5,'sreeni']

d = {'key':'value'}
#dataframe -  tabular data which can be use to perform data analysis

# help(pd.DataFrame())
#syntax
#pd.DataFrame(data=iterable data list/t/dic/se/arra,series)

df = pd.DataFrame(data=ls,columns=['col1'])

print(df)
# top n records
print(df.head(2))
#bottom n records
print(df.tail(2))

print("type of df", type(df))
print("id of df", id(df))

df['col2'] = ['A','B','C','D',1]
df['col1'] = [2,3,4,5,1]
df['sal'] = [500,600,700,800,10]
print("id of df", id(df))
print(df)
# describe will quickly display stats about data
print(df.describe())

#Shape will display no od rows and columns
print(df.shape)
print("No of rows", df.shape[0])
print("No of columns", df.shape[1])

print("all columns",df.columns)

print("datatype columns",df.dtypes)

df2 = df.copy()

df2['sal'] = [500,600,3,4,5]

print(df)
print(df2)

print(df.compare(df2))

d = {'rollno':[1,2,3,5],'name':['A','B','C','D']}

df3 = pd.DataFrame(data=d,columns=['rollno','name'])

print(df3)
print(df3.columns)




