# Databricks notebook source
simpleData = [(1, "James", "Sales", "NY", 90000), \
              (2, "Michael", "Sales", "NY", 86000), \
              (3, "Robert", "Sales", "CA", 81000), \
              (4, "Maria", "Finance", "CA", 90000), \
              (1, "James", "Sales", "NY", 90000)
              ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df1 = spark.createDataFrame(data=simpleData, schema=columns)
df1.printSchema()
df1.show(truncate=False)


simpleData2 = [(1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
df2.printSchema()
df2.show(truncate=False)

# COMMAND ----------

unionDF = df1.union(df2)
unionDF.show(truncate=False)

unionDF_sql = df1.union(df2).distinct()

unionDF_sql.show()

# COMMAND ----------


unionAllDF = df1.unionAll(df2)
unionAllDF.show(truncate=False)

# COMMAND ----------

df1.intersect(df2).show()

# COMMAND ----------

df1.intersectAll(df2).show()

# COMMAND ----------

simpleData = [(1, "James", "Sales", "NY", 90000), \
              (2, "Michael", "Sales", "NY", 86000), \
              (3, "Robert", "Sales", "CA", 81000), \
              (4, "Maria", "Finance", "CA", 90000), \
              (1, "James", "Sales", "NY", 90000)
              ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df1 = spark.createDataFrame(data=simpleData, schema=columns)
df1.show(truncate=False)


simpleData2 = [(1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000), \
                   (1, "James", "Sales", "NY", 90000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
df2.show(truncate=False)

# COMMAND ----------

df1.intersectAll(df2).show()

# COMMAND ----------

df1.intersect(df2).show()

# COMMAND ----------

df1.exceptAll(df2).show()

# COMMAND ----------

simpleData = [(1, "James", "Sales", "NY", 90000), \
              (2, "Michael", "Sales", "NY", 86000), \
              (3, "Robert", "Sales", "CA", 81000), \
              (4, "Maria", "Finance", "CA", 90000), \
              (1, "James", "Sales", "NY", 90000)
              ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df1 = spark.createDataFrame(data=simpleData, schema=columns)
df1.show(truncate=False)


simpleData2 = [(1, "James", "Sales", "NY", 90000), \
               (2, "Michael", "Sales", "NY", 86000), \
               (5, "Sonja", "Sales", "OH", 45000), \
               (6, "Randy H", "Finance", "NJ", 40000)
               ]

columns = ["emp_id", "employee_name", "department", "state", "salary"]
df2 = spark.createDataFrame(data=simpleData2, schema=columns)
df2.show(truncate=False)

# COMMAND ----------

df1.exceptAll(df2).show()

# COMMAND ----------

df1.subtract(df2).show()

# COMMAND ----------

df1 = spark.createDataFrame([("a", 1), ("a", 1), ("a", 1), ("a", 2), ("b", 3), ("c", 4)], ["C1", "C2"])
df2 = spark.createDataFrame([("a", 1), ("b", 3), ("a", 1)], ["C1", "C2"])


# COMMAND ----------

df1.exceptAll(df2).show()

# COMMAND ----------

df1.subtract(df2).show()

# COMMAND ----------

df1 = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

df1.show()

df2 = spark.createDataFrame([(1, "Alice"), (2, "Bob"),(1, "Alice")], ["id", "name"])

df2.show()

# COMMAND ----------

df1.union(df2).show()

# COMMAND ----------

df1.unionAll(df2).show()

# COMMAND ----------

df2.intersect(df1).show()

# COMMAND ----------

df2.intersectAll(df1).show()

# COMMAND ----------

df2.exceptAll(df1).show()

# COMMAND ----------


