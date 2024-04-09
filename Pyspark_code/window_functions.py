# Databricks notebook source
simpleData = (("James", "Sales", 3000), \
              ("Michael", "Sales", 4600), \
              ("Robert", "Sales", 4100), \
              ("Maria", "Finance", 3000), \
              ("James", "Sales", 3000), \
              ("Scott", "Finance", 3300), \
              ("Jen", "Finance", 3900), \
              ("Jeff", "Marketing", 3000), \
              ("Kumar", "Marketing", 2000), \
              ("Saif", "Sales", 4100) \
              )

columns = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import *

# COMMAND ----------

window1 = Window.partitionBy('department').orderBy(df['salary'].desc())

# COMMAND ----------

select a.* , dense_ranK() over( order by salary desc) dense_rank from tb 

select a.* , rank() over( order by salary desc) dense_rank from tb 

select a.* , row_number() over( order by salary desc) dense_rank from tb 
df.withColumn('rank', sum(col('salary')).over(window1)).display()

# COMMAND ----------

df.withColumn('rank', rank().over(Window.partitionBy('department').orderBy(df['salary'].desc()))).display()

# emp.sort(emp.eno.desc(), emp.salary.asc()).show()
# emp.orderBy(emp.eno.asc()).show()
#.withColumn('row_number', row_number().over(window1)).orderBy(df.department.desc()).filter('rank=1')
#withColumn('dense_rank', dense_rank().over(window1))

# COMMAND ----------


