### Day 1-6 - June 18 to June 24
- **Learned:**
- PostgreSQL setup, data types, CSV import
- Window Functions in SQL (Rank, Row Number, Lag, Lead)
- CTEs Queries
- SubQueries, Joins, CaseWhen, Having, Datefunctions
- **File:** `SQL_queries.sql`

### Day 7-8 June 25,26
- **Learned:** PYTHON- groupby, Aggregate, filtering, Merge
- PYTHON- Postgre connection, Data quality checks, date/time operations, string operations
- **File:** `Python_code.ipynb`

### Day 9-14 - June 27 to July 2
**Project 1: Pakistan Climate Analysis ETL**
- Worked with 3 CSV files (Global, Pakistan, Karachi)
- 20 SQL queries, CTEs, window functions from cleaned data .
- CSV | Cleaning through Pandas | Load to Postgre | basic Insights with querys
- Seperate Repo 

**Project 2: PKR Exchange Rate ETL Pipeline**
- Fetched live JSON data from ExchangeRate-API
- Parsed and transformed 8 target currencies, calculated PKR equivalent rates, Loaded to PostgreSQL
- Converted notebook to .py script, automated with Windows Task Scheduler (daily)
- - **File:** `Exchange_rate_ETL_script.py`

### Day 15-18 - July 3 to July 6

**Apache Airflow + Docker**
- Learned Airflow architecture: DAGs, Tasks, Operators, Scheduler
- Converted PKR Exchange Rate pipeline into proper Airflow DAG
- Debugged real issues: port conflicts, .env not loading, 
  container scope, CSV intermediate files between tasks
- Successfully ran 3-task DAG: extract → transform → load
- Data loaded to PostgreSQL automatically via Airflow scheduler
