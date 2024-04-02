# Databricks notebook source
# import pyspark
from pyspark.sql import SparkSession

from pyspark.sql.functions import col,upper, lower, length, concat, initcap, explode, substring, instr,concat_ws, expr

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
df.show(n=5,truncate=25)

df.select(df.firstname, df.lastname).show(5)
df.select(col('firstname'), col('lastname')).show(2)
df.select(df['firstname'], df['lastname'], df['country'], df['state_name']).show(2)
df.select(upper('firstname').alias('fn'), initcap('lastname').alias('ln')).show(5)
df.select(df.colRegex("`^.*name*`")).show(2)
df.select("*").show(2)
df.select("*").filter(" firstname = 'Rahul' ").show()
df.select("*").filter("(firstname = 'Rahul' or lastname ='Rose') and state_name = 'NY' ").show()
df.select((concat(upper(df.firstname),lower(df['lastname']), df.state_name)).alias("FullName"), length(col("state_name")).alias("State_num_letters")).filter("length(state_name) >=2 ").display()
df.select((concat_ws(" ",upper(df.firstname),lower(df['lastname']), df.state_name)).alias("FullName"), length(col("state_name")).alias("State_num_letters")).filter("length(state_name) >=2 ").display()
print("df.columns",df.columns)
print("df.columns[0]",df.columns[0])

selected_with_case = df.select(
    "score",
    "grade",
    expr(
        """
        CASE
            WHEN score >= 90 THEN 'A'
            WHEN score >= 80 THEN 'B'
            WHEN score >= 70 THEN 'C'
            WHEN score >= 60 THEN 'D'
            ELSE 'F'
        END AS grade_letter
        """
    )
)

filtered_df = df.filter(df["Name"].isin(["Alice", "Bob"]))
filtered_df = df.filter((df["Name"].startswith("A")) & (df["Age"] < 40))


# COMMAND ----------

df.createOrReplaceTempView('df')

# COMMAND ----------

spark.sql("select * except(lastname) from df").show()

# COMMAND ----------



# COMMAND ----------

df.createOrReplaceTempView('df')

# COMMAND ----------

df.createTempView("df")

# COMMAND ----------

df.createGlobalTempView("global_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from global_temp.global_view

# COMMAND ----------

df.write.saveAsTable("permanent_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from permanent_view

# COMMAND ----------


from pyspark.sql.functions import col,upper, lower, length, concat, initcap, explode,initcap, substring, instr,concat_ws

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
df.show(n=5,truncate=25)

# COMMAND ----------

df.select('firstname', 'lastname').filter("state_name='CA'")

# COMMAND ----------

df.createOrReplaceTempView("employee")

# COMMAND ----------

# MAGIC %sql
# MAGIC select upper(firstname), substr(lastname,1,2), length(country) from employee where state_name='CA'

# COMMAND ----------

spark.sql("select upper(firstname), substr(lastname,1,2), length(country) from employee where state_name='CA'").display()

# COMMAND ----------

df.createTempView('employee2')

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employee2 limit 4

# COMMAND ----------

df.createGlobalTempView('global_employee')

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from global_temp.global_employee

# COMMAND ----------

df.write.saveAsTable("employee")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employee

# COMMAND ----------

df.display()

# COMMAND ----------

df.select(upper('firstname').alias('firstname'), 'lastname', 'country').display()

# COMMAND ----------

df.select(col('firstname'), col('lastname')).show(2)

# COMMAND ----------

df.select(df['firstname'], df['lastname'], df['country'], df['state_name']).display()

# COMMAND ----------

df.select(df.firstname, df.lastname).show(5)

# COMMAND ----------

df.select("*").show(2)

df.show(2)

# COMMAND ----------

df.select(df.colRegex("`^.*name*`")).show(2)

# COMMAND ----------

selected_with_case = df.select(
    "firstname",
    "lastname",
    expr(
        """
        CASE
            WHEN length(state_name) = 1 THEN 'NJ'
            ELSE 'NY'
        END AS statecode
        """
    )
)

# COMMAND ----------

selected_with_case.display()

# COMMAND ----------

df.display()

# COMMAND ----------

df.filter("state_name ='C' and state_name='NY' ").show()

# COMMAND ----------

df.where(" state_name in ('NY', 'CA') ").show()

# COMMAND ----------

filtered_df = df.filter(df["state_name"].isin(["CA", "NY"]))
#filtered_df = df.filter((df["Name"].startswith("A")) & (df["Age"] < 40))
filtered_df.show()

# COMMAND ----------

df.select((concat_ws(" ",upper(df.firstname),lower(df['lastname']), df.state_name)).alias("FullName"), length(col("state_name")).alias("State_num_letters")).filter("length(state_name) >=2 ").display()

# COMMAND ----------


# MAGIC %sql
# MAGIC
# MAGIC select * from global_temp.global_view

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC update employee set country='US' where state_name='A'

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY employee

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT max(version) -1 as permanent_view  FROM (DESCRIBE HISTORY permanent_view)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC RESTORE TABLE employee  TO VERSION AS OF 0

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employee2 limit 4

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from global_temp.global_employee

# COMMAND ----------

