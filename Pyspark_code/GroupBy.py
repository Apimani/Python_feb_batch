# Databricks notebook source
#select c1,c2, sum(c1) from tn where group by c1,c2 having order by

# COMMAND ----------

from pyspark.sql.functions import sum, avg, min, col, max, count, upper, lower, regexp_replace


simpleData = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  ]

schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=simpleData, schema = schema)
df.printSchema()
df.show(truncate=False)



# COMMAND ----------

summary = df.select(df.salary, df['age'], 'bonus').summary().where("summary in ('count', 'mean') ")

summary.display()

#help(df.summary)

# COMMAND ----------

df.select(sum(col('salary')).alias("sum_sal"), count("*").alias("num_of_records"), \
          avg(df.bonus).alias("average_sal"), min('salary').alias("min_sal"), max(df.salary).alias("max_sal")).display()

# COMMAND ----------

df.createOrReplaceTempView("source123")

# COMMAND ----------

print(id(df))

# COMMAND ----------

df = df.withColumn('department', upper(df.department))

# COMMAND ----------

df.display()

# COMMAND ----------

print(id(df))

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select department,count(*), sum(salary), min(salary) from source123 group by department having count(*)>1

# COMMAND ----------

df4 = spark.sql(" select department,count(*), sum(salary), min(salary) from source123 group by department")

df4.show()

# COMMAND ----------

df.groupBy('department').count().show()

# COMMAND ----------

#df.groupBy("department").count().display()


df2 = df.groupBy("department","state").sum('bonus')

df2.groupBy('department').count().show()

# COMMAND ----------

df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"), \
         avg("salary").alias("avg_salary"), \
         sum("bonus").alias("sum_bonus"), \
         max("bonus").alias("max_bonus"), \
        min("salary"), \
        count('department')
     ) \
    .show(truncate=False)
    


# COMMAND ----------

df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"), \
      avg("salary").alias("avg_salary"), \
      sum("bonus").alias("sum_bonus"), \
      max("bonus").alias("max_bonus")) \
    .where(col("sum_bonus") >= 50000) \
    .sort(col('department').desc()).show()

# COMMAND ----------

data = [(1,'Sreeni'),(2,'rahul'),(3,'Mani'),(3,'Mani'),(1,'rahul')]

schema = ['id', 'name']

df = spark.createDataFrame(data=data, schema=schema)

df.show()

# COMMAND ----------

df.distinct().display()

# COMMAND ----------

df2 = df.dropDuplicates()

df2.display()

# COMMAND ----------

df.show()

# COMMAND ----------

df.dropDuplicates(['id','name']).show()

# COMMAND ----------

df.show()

# COMMAND ----------

df.groupBy('department').pivot('state').count().display()

# COMMAND ----------

df.groupBy('department','state').count().display()

# COMMAND ----------

df2 = df.groupBy('department').pivot('state').count()

# COMMAND ----------


