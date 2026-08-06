# tempview,parquetsparksql,windowfunc
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import functions as F

spark=SparkSession.builder\
   .appName("Payroll_analytics")\
   .master("local[*]")\
   .getOrCreate()

emp=spark.read.json("D:\\Data-Engg-Work\\databricks\\structjsonsample.json")
dept=spark.read.json("D:\\Data-Engg-Work\\databricks\\departments.json")

joinjson=emp.join(
     dept,
    "Dept",
    "left"
)

joinjson.createOrReplaceTempView("Employees")

result=spark.sql('''
    WITH emp AS(
        SELECT id,name,Dept,salary,address,manager_name,
        RANK() OVER(PARTITION BY Dept ORDER BY salary DESC) AS Ranked_salary
        FROM Employees
    )
    SELECT * FROM emp
    WHERE Ranked_salary=1;
''')
result.show()

# result.write.parquet("D:/Data-Engg-Work/databricks/output")
# result2 = spark.read.parquet("D:/Data-Engg-Work/databricks/output")

# casting=joinjson.select("id","name","Dept",joinjson.salary.cast("integer").alias("salary"),"address","manager_name")
# result=casting.fillna({"manager_name":"Not Assigned"})
# groupbyy=result.groupBy("Dept").agg(
#     F.count("*").alias("employee_count"),
#     F.avg("salary").alias("avg_salary")
# )

# orderbyy=groupbyy.orderBy(groupbyy.avg_salary.desc())            

# orderbyy.show()
