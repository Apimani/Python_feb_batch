# Databricks notebook source
# DBTITLE 1,This is code to create simple spark dataframe using list of tuple values
emp = [(1, "Smith", -1, "2018", "10", "M", 3000), \
       (2, "Rose", 1, "2010", "20", "M", 4000), \
       (3, "Williams", 1, "2010", "30", "M", 1000), \
       (4, "Jones", 10, "2005", "10", "F", 2000), \
       (5, "Brown", 2, "2010", "40", "", 1000), \
       (6, "Brown", 2, "2010", "50", "", 500) \
       ]
empColumns = ["eno", "ename", "mgr_id", "year_joined", \
              "dept_id", "gender", "salary"]

emp = spark.createDataFrame(data=emp, schema=empColumns)
emp.printSchema()
emp.show(truncate=False)

dept = [("Finance", 10), \
        ("Marketing", 20), \
        ("Sales", 30), \
        ("IT", 40),
        ("HR", 60) \
        ]
deptColumns = ["dept_name", "dept_id"]
dept = spark.createDataFrame(data=dept, schema=deptColumns)
dept.printSchema()
dept.show(truncate=False)

# COMMAND ----------

join_df = emp.join(dept, emp.dept_id == dept.dept_id, 'inner')

join_df.display()

# COMMAND ----------

emp.join(dept, 'dept_id', 'inner').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'left').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'right').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'full').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'leftsemi').show() 

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'leftanti').show() 

# COMMAND ----------


