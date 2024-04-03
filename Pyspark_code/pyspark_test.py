from pyspark.sql import SparkSession

from pyspark.sql.types import StructType, IntegerType, FloatType, LongType, StructField, StringType

# Create SparkSession
spark = (SparkSession.builder
      .getOrCreate())


# a='string'
# print(dir(a))

# print(type(spark))
#
# print(dir(spark))
#
# print(help(spark.createDataFrame))

dataList1 = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
df=spark.createDataFrame(dataList1, schema=['Language2','fee2'])
df.show()
print(df.count())
df.printSchema()

print("*"*30)
schema2 = 'language string, fee integer'

dataList2 = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
df2=spark.createDataFrame(dataList2, schema=schema2)
df2.show()
print(df2.count())
df2.printSchema()



schema = ['language' , 'fee']

schema3 = StructType([StructField("id",StringType(),nullable=False),
                     StructField("name", StringType(), nullable=True),
                     StructField('age',IntegerType(),nullable=False)
                     ])

dataList3 = [("Java", 20000,21), ("Python", 100000,22), ("Scala", 3000,23)]
df3 = spark.createDataFrame(dataList3, schema3)

df3.display()

df3.show()

print(df3.schema.json())

print(df.collect())




