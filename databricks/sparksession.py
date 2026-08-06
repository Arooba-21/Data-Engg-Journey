#automatically on databricks 
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("MyFirstSparkApp")
    .master("local[*]")
    .getOrCreate()
)

print("Spark is running!")
spark.stop()