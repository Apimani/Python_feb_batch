import logging

import pandas as pd

# 1. CRITICAL==>50==>Represents a very serious problem that needs high attention
# 2. ERROR===>40===>Represents a serious error
# 3. WARNING==>30==>Represents a warning message, some caution needed. It is alert to
# the programmer
# 4. INFO===>20===>Represents a message with some important information
# 5. DEBUG===>10==>Represents a message with debugging information
# 6. NOTSET==>0==>Rrepresents that the level is not set.


# %(asctime)s: The timestamp of the log message in the format specified by the datefmt parameter (if provided).
# %(levelname)s: The log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
# %(message)s: The log message itself.
# %(name)s: The name of the logger.
# %(filename)s: The name of the file containing the logger call.
# %(lineno)d: The line number where the logger call occurred.
# %(funcName)s: The name of the function/method where the logger call occurred.

# Default level is Warning

logging.basicConfig(filename='new.txt', filemode='w',level=logging.ERROR,
                   format='%(asctime)s - %(levelname)s - %(message)s - %(name)s-%(funcName)s-%(lineno)d')

logger = logging.getLogger()
# print("starting...")
# logger.debug("debug") #
# #print("print debug")
# logger.info("km travelled")
# print("print km travelled")
# logger.warning("had to diversion")
# print("print had to take diversion")
# logger.error("car type puncture")
# print("print car puncture")
# logger.critical("print taken another mode of travel")
# print("taken another mode of tarvel")
# logger.info("this second info")
# print("end of journey....")
def read(file_type, path):
    if file_type =='csv':
        df = pd.read_csv(path)
        #print("Data has been read successfully and file path is " , path )
        logger.info("Data has been read successfully and file path is ")
        return df

    elif file_type == 'excel':
        df = pd.read_excel(path)
        #print("Data has been read successfully and file path is " , path )
        logger.info("Data has been read successfully and file path is ")
        return df
    else:
        print("Please enter correct file type")
        logger.error(f"please enter correct file format, Current {file_type} is not handled")


df = read('csv', r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\Contact_info.csv")
print(df.head())
df2 = read('excel', r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\test.xlsx")
print(df2.head())

df3 = read("parquet", 'xyz.parquet')