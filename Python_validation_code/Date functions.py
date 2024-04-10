# Databricks notebook source

from pyspark.sql.functions import *
data = [["1", "2020-02-01"], ["2", "2019-03-01"], ["3", "2021-03-01"]]
df = spark.createDataFrame(data, ["id", "create_date"])
df.show()
df.printSchema()


df.select(current_timestamp().alias("current_date")).show(1)


df.select(col("create_date"),date_format(col("create_date"), "MMM-dd-yy").alias("date_format")).show() # to_char(date, 'YYYY-MON-dd')

# COMMAND ----------

df.select('create_date',
          to_date(col("create_date"), "yyyy-dd-MM").alias("to_date")
          ).select('to_date',date_format(col("to_date"), "MMM-dd-yyyy").alias("dsiplay_format")).show()

# COMMAND ----------

df.select(col("create_date"),
          datediff(current_date(), col("create_date")).alias("datediff")
          ).show()

# COMMAND ----------

df.select(col("create_date"),
          months_between(current_date(), col("create_date")).alias("months_between")
          ).show()

# COMMAND ----------

df.select(col("create_date"),
          add_months(col("create_date"), 3).alias("add_months"),
          add_months(col("create_date"), -3).alias("sub_months"),
          date_add(col("create_date"), 4).alias("date_add"),
          date_sub(col("create_date"), 4).alias("date_sub")
          ).show()

# COMMAND ----------

df.select(col("create_date"),
          year(col("create_date")).alias("year"),
          month(col("create_date")).alias("month"),
          next_day(col("create_date"), "Sunday").alias("next_day"),
          weekofyear(col("create_date")).alias("weekofyear"),
          quarter(col("create_date")).alias("quarter")
          ).filter('year=2020').show()

# COMMAND ----------


df.select(col("create_date"),
          dayofweek(col("create_date")).alias("dayofweek"),
          dayofmonth(col("create_date")).alias("dayofmonth"),
          dayofyear(col("create_date")).alias("dayofyear"),
          ).show()

# COMMAND ----------

data = [["1", "2020-02-01 11:01:19.06"], ["2", "2019-03-01 12:01:19.406"], ["3", "2021-03-01 12:01:19.406"]]
df3 = spark.createDataFrame(data, ["id", "create_date"])
df3.show(truncate=False)

# COMMAND ----------

df3.select(col("create_date"),
           hour(col("create_date")).alias("hour"),
           minute(col("create_date")).alias("minute"),
           second(col("create_date")).alias("second")
           ).show(truncate=False)

# COMMAND ----------

# Import necessary libraries
from pyspark.sql import SparkSession


# Create a sample DataFrame
data = [("Alice", "Math", 90), ("Alice", "English", 85),
        ("Bob", "social", 80), ("Bob", "Science", 88)]

df = spark.createDataFrame(data, ["Name", "Subject", "Score"])
df.show()
# Pivot the data
pivot_df = df.groupBy("Name").pivot("Subject").sum("Score")

# Show the resulting DataFrame
pivot_df.show()


# COMMAND ----------

unpivot_df = pivot_df.selectExpr("Name", "stack(4, 'Math', Math, 'Science', Science,'social',social,'English', English) as (Subject, Score)")

# Show the resulting DataFrame
unpivot_df.filter('Score is not null').show()

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

from pyspark.sql.functions import upper, lower, substring, instr, lead, round, initcap, lpad, trim, 



data = [("John", "1234567890"), ("Alice", "9876543210")]
df = spark.createDataFrame(data, ["Name", "PhoneNumber"])

df.select(upper(df.Name)).show()

def format_phone_number(phone_number):
    # Assuming phone_number is a 10-digit string
    formatted_number = "+1 (%s) %s-%s" % (phone_number[:3], phone_number[3:6], phone_number[6:])
    return formatted_number


print(format_phone_number('1234566'))



format_phone_number_udf2 = udf(format_phone_number)

# Apply the UDF to the DataFrame
df.withColumn("FormattedPhoneNumber", format_phone_number_udf2(df["PhoneNumber"])).show()

df.select("PhoneNumber", format_phone_number_udf2(df["PhoneNumber"])).show()





# COMMAND ----------

df.createOrReplaceTempView('df')

# COMMAND ----------

# MAGIC %sql
# MAGIC select upper(name), lower(name),format_phone_number_udf2(PhoneNumber) from df

# COMMAND ----------

from pyspark.sql.functions import *
spark.udf.register("format_phone_number_udf2", format_phone_number_udf2)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select upper(name), lower(name),format_phone_number_udf2(PhoneNumber) conv_num from df

# COMMAND ----------

spark.sql("select upper(name), lower(name),format_phone_number_udf2(PhoneNumber) conv_num from df").show()

# COMMAND ----------

data = [("John", ["apple", "banana", "orange"]),
        ("Alice", ["grape", "apple", "kiwi"]),
        ("Bob", ["melon", "pineapple"])]

df = spark.createDataFrame(data, ["Name", "Fruits"])

df.show()

# Check if the array contains a specific element
result_df = df.select("Name", "Fruits", array_contains(df["Fruits"], "apple").alias("HasApple"))

# Show the result DataFrame
result_df.filter("HasApple = True").show()

# COMMAND ----------

result_df.filter('HasApple = false').show()

# COMMAND ----------


