#simple json file
# from pyspark.sql import SparkSession

# spark=SparkSession.builder\
#          .appName("JSON format")\
#          .master("local[*]")\
#          .getOrCreate()

# df=spark.read.json("D:\\Data-Engg-Work\\sample.json")
# df_select=df.select("name","salary")
# df_select.show()
# df_select.printSchema()

#if struct structure
from pyspark.sql import SparkSession

spark=SparkSession.builder\
         .appName("JSON format")\
         .master("local[*]")\
         .getOrCreate()

df=spark.read.json("D:\\Data-Engg-Work\\databricks\\struct json sample.json")
df_select=df.select("name", "address.city", "address.zip")
df_select.show()
df_select.printSchema()