from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import functions as F

spark=SparkSession.builder\
   .appName("Payroll_analytics")\
   .master("local[*]")\
   .getOrCreate()
df=spark.read.json("D:\\Data-Engg-Work\\databricks\\structjsonsample.json")

df.createOrReplaceTempView("employees")

# result = spark.sql("SELECT Dept, AVG(salary) FROM employees GROUP BY Dept HAVING AVG(salary)>80000")
# result.show()

result = spark.sql("""
    WITH ranked_employees AS (
        SELECT id, name, Dept, salary,
               RANK() OVER (PARTITION BY Dept ORDER BY salary DESC) AS salary_rank
        FROM employees
    )
    SELECT id, name, Dept, salary, salary_rank
    FROM ranked_employees
    WHERE salary_rank = 1
""")

result.show()