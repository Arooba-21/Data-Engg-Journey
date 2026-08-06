from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import functions as F
from pyspark.sql.functions import broadcast

spark=SparkSession.builder\
   .appName("Payroll_analytics")\
   .master("local[*]")\
   .getOrCreate()

emp=spark.read.json("D:\\Data-Engg-Work\\databricks\\structjsonsample.json")
dept=spark.read.json("D:\\Data-Engg-Work\\databricks\\departments.json")

# print(emp.rdd.getNumPartitions())

# emp_repartitioned = emp.repartition(4)
# print(emp_repartitioned.rdd.getNumPartitions())

# df_cached = emp.cache()
# df_cached.count()
# df_cached.show()
# df_cached.unpersist()

result=emp.join(dept, "Dept", "left")
# result = emp.join(broadcast(dept), "Dept", "left")
result.explain()