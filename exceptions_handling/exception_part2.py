import logging
import pandas as pd
a = 10
b = 20

print("Hello world")
try:
    print("division of two number", a/b)
except ZeroDivisionError as e:
    print("division is not possible with zero", e)
    logging.error("Zero division")
except TypeError as e:
    print("division is not possible with un supported type", e)
    logging.error("type error")
except :
    print("This is default exception")
    logging.error("default", a,b)

try:
    df = pd.read_csv(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\Contact_info2.csv", nrows=10)
    print(df.head(2))
except FileNotFoundError as e:
    df = pd.read_csv(
        r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\Contact_info.csv",
        nrows=10)
    print(df.head(2))
    print("file not found", e)
    logging.error("File not found")
except:
    print("default")

#df = pd.read_csv(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\Contact_info.csv", nrows=5)

print("End of python code")