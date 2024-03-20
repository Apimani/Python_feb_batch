import pandas as pd
import openpyxl
import pyarrow

help(pd.read_csv)

df = pd.read_csv(filepath_or_buffer="C:\\Users\\A4952\\Downloads\\Python_feb_batch-20240218T160531Z-001\\Python_feb_batch\\Files\\Contact_info.csv")

df2 = pd.read_csv(filepath_or_buffer="C:/Users/A4952/Downloads/Python_feb_batch-20240218T160531Z-001/Python_feb_batch/Files/Contact_info.csv")
# #
df = pd.read_csv(filepath_or_buffer="C:\Users\A4952\PycharmProjects\pythonProject\source_files\Contact_info_t.csv", nrows=5,sep=',')
print(df)
print(df2)
print(df)

print(df.shape)

help(pd.read_parquet)

#df = pd.read_excel(io=r"C:\Users\A4952\Desktop\New Microsoft Excel Worksheet.xlsx", nrows=5)

df = pd.read_parquet(r"C:\Users\A4952\PycharmProjects\pythonProject\source_files\userdata1.parquet")


# print(df.shape)
print(df)

print("value_count", df.value_counts())