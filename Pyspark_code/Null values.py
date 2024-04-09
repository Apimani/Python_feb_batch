# Databricks notebook source
df = spark.read.csv("dbfs:/FileStore/parquet/Contact_info.csv", header=True)

# COMMAND ----------

df.display()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.fillna('unkwn').display()

# COMMAND ----------

df.fillna(1).display()

# COMMAND ----------

df2 = spark.read.csv("dbfs:/FileStore/shared_uploads/csv_files/Contact_info-1.csv", header=True, inferSchema=True)

df2.printSchema()

# COMMAND ----------

df2.display()

# COMMAND ----------

df2.na.fill('unknw').display()

# COMMAND ----------

df2.fillna(100).fillna('default').display()

# COMMAND ----------

df2.createOrReplaceTempView('df')

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select nvl(identifier,100), surname, nvl(middle_initial,'default'), nvl(Primary_street_number,'default') from df

# COMMAND ----------

from pyspark.sql.functions import when,col, upper
df3 = df2.withColumn('Primary_street_number', when(upper(col('Primary_street_number'))=='NULL',None).otherwise(col('Primary_street_number'))) #.fillna('unknwn').fillna(1)

# COMMAND ----------

from pyspark.sql.functions import col, sum

df3.select([sum(col(c).isNull().cast('int')).alias(c) for c in df.columns]).display()

# COMMAND ----------



# Count null values in each column
null_counts = df.select([sum(col(c).isNull().cast('int')).alias(c) for c in df.columns])
null_counts.display()

# COMMAND ----------

from pyspark.sql.functions import upper, trim

df2 = df2.withColumn('Primary_street_number', when((upper(df2['Primary_street_number']) == "NULL") | (trim(df2['Primary_street_number']) == "" ) |
                                                   (trim(df2['Primary_street_number']) == "NA" ) , None).otherwise(df2['Primary_street_number']))

df2.display()




# COMMAND ----------

df3 = df2.withColumn('Primary_street_number', when( (upper(col('Primary_street_number'))=='NULL')   | (trim(col('Primary_street_number')) =='' ), None).otherwise(col('Primary_street_number'))).fillna('unknwn').fillna(0).display()

# COMMAND ----------

df2.display()



# COMMAND ----------

type(df4)

# COMMAND ----------



# COMMAND ----------

collect_out = df.collect()

type(collect_out)

# COMMAND ----------

print(collect_out)

print(len(collect_out))

collect_out[0]

# COMMAND ----------

collect_out[0]['Primary_street_number']

# COMMAND ----------

df4.select("Primary_street_number").filter('identifier=1').collect()[0][0]

# COMMAND ----------

df4.display()

# COMMAND ----------

df4.sample(0.2, seed=4).display()

# COMMAND ----------

df.sample(fraction=0.3, seed=8, withReplacement=True).display()

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.select('identifier', 'surname').display()

# COMMAND ----------

df= df.drop('Surname')

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.drop('given_name', 'suffix','identifier')

# COMMAND ----------

df.display()

# COMMAND ----------

df4 = spark.read.csv("dbfs:/FileStore/shared_uploads/csv_files/Contact_info-1.csv", header=True, inferSchema=True)

df4.display()

# COMMAND ----------

df4.createOrReplaceTempView('df4')

# COMMAND ----------

spark.sql("select distinct * from df4").display()

# COMMAND ----------

df.distinct().display()

# COMMAND ----------

df.dropDuplicates(['city']).display()

df.dropDuplicates().display()

# COMMAND ----------


