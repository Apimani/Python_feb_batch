import pandas as pd
from pandasql import sqldf

data = {'id':[1,2,3,4,5,6,1,2,2,2], 'marks':[89,23,12,17,18,90,87,89,11,90]}

df = pd.DataFrame(data=data)

print(df)

print(df.groupby(['id']).sum('marks'))
print(df.groupby('id').max('marks'))
print(df.groupby('id').min('marks'))
print(df.groupby('id').mean('marks'))
print(df.groupby('id').count())


# Group by 'id' and calculate various aggregate functions
grouped_df = df.groupby('id').agg({
    'marks': ['sum', 'mean', 'min', 'max', 'count']
})

print(grouped_df)


dict1={'cust':['x','y','z','k','r'],'prod_code':[1,2,3,6,7]}
dict2={'cust':['a','z','w','v'],'prod_code':['KA','TN','MH','AP']}
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)

print(df1)
print(df2)

print("pandas concat")
print(pd.concat([df1, df2])) # unionAll operation # vertical adding of two df

print("pandas concat with axis=1")
print(pd.concat([df1, df2], axis=1)) # unionAll operation # vertical adding of two df


print(pd.merge(df1,df2,on='cust', how='inner'))
print("left join")
print(pd.merge(df1,df2,on='cust', how='left'))
print("right join")
print(pd.merge(df1,df2,on='cust', how='right'))
print("full join")
print(pd.merge(df1,df2,on='cust', how='outer',suffixes=['_left','_right']))

join=pd.merge(df1,df2,on='cust', how='outer',suffixes=['_left','_right'])

# print(df)
# print(df['id'].nunique())

join['prod_code_left']= join['prod_code_left'].fillna('999')
join['prod_code_right']= join['prod_code_right'].fillna('UNKNWN')

print(join)
df = pd.read_csv(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\Employee.csv")
# print(df)
# print(df.iloc[2:7,])
# print(df.iloc[: , 0:2])
# print(df[['Identifier','Surname']])
# print(df)
# print(df.loc[1:5,'Identifier':'birthmonth'])
#
# print(df[((df.Identifier == 6 ) & (df.Surname == 'Raheem')) | (df.birthmonth >=198904 )])


print(sqldf("""select identifier, count(1) as cnt from df 
             group by identifier """))















