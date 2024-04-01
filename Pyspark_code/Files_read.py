# Databricks notebook source
df2 = spark.read.option("multiline", "True").json("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample1.json")
df2.display()

print(df2.count())

df.columns

# COMMAND ----------

df1 = spark.read.format("json").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/singleline-2.json")

df1.display()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df1 = spark.read.format("json").option("multiline", "True").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample4.json")

df1.display()

# COMMAND ----------

df1.printSchema()

# COMMAND ----------

from pyspark.sql.functions import explode, upper,lower, instr, lead,lag, substring, length

# COMMAND ----------

df2 = df1.select("*", explode("people").alias("colum")).drop("people")

# COMMAND ----------

df2.display()

# COMMAND ----------

df2.printSchema()

# COMMAND ----------

df3 = df2.select(df2.colum.age.alias("age"), df2.colum.firstName, df2.colum.gender, df2.colum.lastName, df2.colum.number)

df3.display()

# COMMAND ----------

df5 = spark.read.format("json").option("multiline", "True").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample4.json")

df5.display()

# COMMAND ----------

def flatten(df):
    # compute Complex Fields (Lists and Structs) in Schema
    complex_fields = dict([(field.name, field.dataType)
                           for field in df.schema.fields
                           if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]
        print("Processing :" + col_name + " Type : " + str(type(complex_fields[col_name])))

        # if StructType then convert all sub element to columns.
        # i.e. flatten structs
        if type(complex_fields[col_name]) == StructType:
            expanded = [col(col_name + '.' + k).alias(col_name + '_' + k) for k in
                        [n.name for n in complex_fields[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        # if ArrayType then add the Array Elements as Rows using the explode function
        # i.e. explode Arrays
        elif type(complex_fields[col_name]) == ArrayType:
            df = df.withColumn(col_name, explode_outer(col_name))

        # recompute remaining Complex Fields in Schema
        complex_fields = dict([(field.name, field.dataType)
                               for field in df.schema.fields
                               if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    return df


# COMMAND ----------

df6 = flatten(df5)

df6.display()

# COMMAND ----------

df6.printSchema()

# COMMAND ----------



# COMMAND ----------

df1 = spark.read.option("multiline", "True").json("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample2.json")

df1.display()

# COMMAND ----------

df2 = df1.select("*", explode("phoneNumbers").alias("phone")).drop("phoneNumbers")
df2.printSchema()

# COMMAND ----------

df2.display()

# COMMAND ----------

df2.select(df2.address.city, df2.address.state, df2.age, df2.firstName, df2.gender, df2.lastName, df2.phone.number, df2.phone.type).display()

# COMMAND ----------

df1 = spark.read.option("multiline", "True").json("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample2.json")

df1.display()

# COMMAND ----------

def flatten(df):
    # compute Complex Fields (Lists and Structs) in Schema
    complex_fields = dict([(field.name, field.dataType)
                           for field in df.schema.fields
                           if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]
        print("Processing :" + col_name + " Type : " + str(type(complex_fields[col_name])))

        # if StructType then convert all sub element to columns.
        # i.e. flatten structs
        if type(complex_fields[col_name]) == StructType:
            expanded = [col(col_name + '.' + k).alias(col_name + '_' + k) for k in
                        [n.name for n in complex_fields[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        # if ArrayType then add the Array Elements as Rows using the explode function
        # i.e. explode Arrays
        elif type(complex_fields[col_name]) == ArrayType:
            df = df.withColumn(col_name, explode_outer(col_name))

        # recompute remaining Complex Fields in Schema
        complex_fields = dict([(field.name, field.dataType)
                               for field in df.schema.fields
                               if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    return df


# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import col, explode_outer

df2 = flatten(df1)

df2.display()

# COMMAND ----------

df = spark.read.parquet("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/parquet/userdata1.parquet")

df.display()

df.printSchema()

# COMMAND ----------

df = spark.read.format("avro").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/userdata1.avro")

df.printSchema()

df.display()

# COMMAND ----------

df = spark.read.format('parquet').load("dbfs:/FileStore/parquet/userdata1.parquet")
df.display()
df.printSchema()

print(df.count())

# COMMAND ----------

df = spark.read.format('parquet').load("dbfs:/FileStore/parquet/*.parquet")
df.display()
df.printSchema()

print(df.count())

# COMMAND ----------

df = spark.read.format('csv').load("dbfs:/FileStore/parquet/*.csv", header= True)
display(df)
df.printSchema()

print(df.count())

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TEMPORARY VIEW parquetTable
# MAGIC USING org.apache.spark.sql.parquet
# MAGIC OPTIONS (
# MAGIC   path "dbfs:/FileStore/parquet/userdata1.parquet"
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM parquetTable where id=1

# COMMAND ----------

df = spark.read.format('avro').load("dbfs:/FileStore/avro/userdata1.avro")

df.display()

print(df.count())

df.printSchema()

# COMMAND ----------


data = [("Rahul","Smith","USA","C"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("ramesh","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("rahul","Smith","USA","A"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("Jamessadhfsadhgasfghashgfashdgfghsadfa","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","K"),
    ("Maria","Jones","USA","FL")
  ]

columns = ["firstname","lastname","country","state_name"]
df = spark.createDataFrame(data = data, schema = columns)
df.show(n=2,truncate=False)

# COMMAND ----------

df.count()

# COMMAND ----------

df.rdd.getNumPartitions()

# COMMAND ----------

df.write.csv("dbfs:/FileStore/csvload2/employee2.csv", mode='append', header=True)

# COMMAND ----------

df.write.parquet("dbfs:/FileStore/parload/employee.parquet", mode='append')

# COMMAND ----------

df.write.csv("dbfs:/FileStore/csvload/employee.csv", mode='overwrite')

# COMMAND ----------

spark.read.csv("dbfs:/FileStore/csvload2/employee2.csv", header=True).display()

# COMMAND ----------


