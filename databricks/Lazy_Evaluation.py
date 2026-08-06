from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyFirstSparkApp") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("D:\\Data-Engg-Work\\sample.csv", header=True, inferSchema=True)

select_df = df.select("name", "salary")
select_df.show()
