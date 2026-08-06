from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark=SparkSession.builder\
   .appName("Payroll_analytics")\
   .master("local[*]")\
   .getOrCreate()

emp=spark.read.json("D:\\Data-Engg-Work\\databricks\\structjsonsample.json")
casting=emp.select("id","name","Dept",emp.salary.cast("integer").alias("salary"))
casting.write.parquet("D:/Data-Engg-Work/databricks/casting_output")
result = spark.read.parquet("D:/Data-Engg-Work/databricks/casting_output")
result.printSchema()