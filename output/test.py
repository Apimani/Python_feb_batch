from pyspark.sql import SparkSession
spark = (SparkSession.builder
      .getOrCreate())
dataList1 = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
df=spark.createDataFrame(dataList1, schema=['Language2','fee2'])
df.show()

df.coalesce(1).write.csv(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\output\test2.csv", mode='append')
# (df.coalesce(1).write
#     .format("csv")
#     .option("header", "true")
#     .mode("append")
#     .save(r"test2.csv"))

spark.read.csv(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\output\test2.csv").coalesce(1).\
      write.csv(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\output\test3.csv", mode='append')