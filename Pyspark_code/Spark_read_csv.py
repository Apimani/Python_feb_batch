from pyspark.sql import SparkSession

from pyspark.sql.types import StructType, IntegerType, FloatType, LongType, StructField, StringType
spark = (SparkSession.builder
      .getOrCreate())

df1 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/IPL_Matches_2008_2020-2.csv")

df1.display()

from pyspark.sql.functions import spark_partition_id, asc, desc
df1\
    .withColumn("partitionId", spark_partition_id()) \
    .groupBy("partitionId")\
    .count()\
    .orderBy(asc("count"))\
    .show()
path="dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/IPL_Ball_by_Ball_2008_2020.csv"
#Read a csv with delimiter, the default delimiter is ","
df3=spark.read.option("delimiter",",").option("header",True).csv(path)
df3.display()
# df4=spark.read.option("delimiter",",").option("header",True).csv(["dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/Titanic2.csv","dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/Titanic1.csv"])
# df4.display()

# df4=spark.read.option("delimiter",",").option("header",True).csv("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/Titanic2.csv")
# df4.display()



df4=spark.read.option("delimiter",",").option("header",True).csv("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/*.csv")
df4.display()
df5=spark.read.option("delimiter",",").option("header",True).csv("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com")
df5.display()
print(df5.count())
df4=spark.read.options(delimiter=",",header=True).csv("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/Titanic2.csv")

df4.display()