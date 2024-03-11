import pandas as pd

a=10


# try:
#     print("a divide by b is", a/b)
# except ZeroDivisionError as e:
#     print("Can divide with zero",e)
# except TypeError as e:
#     print("Type of a or b is not interger/numeric", e)
# except  NameError as e:
#     print("a or b is not defined", e)
#
# print("This is end")

# try:
#     df = pd.read_csv(r"C:\Users\A4952\Desktop\Contact_info_t2.csv", nrows=10)
#     print(df.head(2))
# except FileNotFoundError as E:
#     print("File is not found in specified location", E)
#     df = pd.read_csv(r"C:\Users\A4952\Desktop\Contact_info_t.csv", nrows=5)

try:
    with open(r"C:\Users\A4952\Desktop\text_file.txt", 'r') as f:
        file = f.read()
        print(file)
        f.close()
except:
    print("file was not present")
finally:
    print("finally printing")


