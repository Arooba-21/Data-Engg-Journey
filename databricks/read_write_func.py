#with column,alias,cast,groupby,joins,orderby
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, max
spark=SparkSession.builder\
      .appName("! program")\
      .master("local[*]")\
      .getOrCreate()

df=spark.read.json("D:\\Data-Engg-Work\\databricks\\structjsonsample.json")
dept_df=spark.read.json("D:\\Data-Engg-Work\\databricks\\departments.json")
final=df.select("id", "name", "Dept",df.salary.cast("integer").alias("monthly_income"), "address.city", "address.zip")
#final.printSchema()
#final.show()

fin=df.groupBy("Dept").agg(
    count("*").alias("employee_count"),
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary")
)
#fin.show()

result = df.join(
    dept_df,"Dept",
    "left"  
)
#result.show()

orderby=df.orderBy(df.salary.desc()).limit(3) 
orderby=df.dropDuplicates(["id"]) 
orderby=df.na.fill({"dept": "Unknown"})            
orderby.show()     

spark.stop()