# Databricks notebook source
from pyspark.sql.functions import lit

df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

df.show()


# COMMAND ----------

df.createOrReplaceTempView('df')

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select id, name, 30 as Age from df

# COMMAND ----------

# Add a new column 'age' with a constant value
df2 = df.withColumn("age", lit(20))

df2.show()

# COMMAND ----------

from pyspark.sql.functions import col, upper, expr

# Update the 'name' column to uppercase
df= df.withColumn("name", upper(col("name")))

df.show()


# COMMAND ----------

df4 = df.withColumn("roll_num_word", expr('''case when id=1 then 'one' else 'two' end roll_num_word''' ))

df4.show()

# COMMAND ----------

df4 = df.withColumn("dense_rank", expr('''dense_rank() over(order by id desc)''' ))

df4.show()

# COMMAND ----------

df4 = df4.withColumnRenamed("name","first_name").withColumnRenamed('dense_rank','position')

df4.show()

# COMMAND ----------

df4.show()

# COMMAND ----------


