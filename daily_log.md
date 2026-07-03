### Day 1 - June 18
- **Learned:** PostgreSQL setup, data types, CSV import
- **Struggle:** Unterminated quote error ,manually fixed via Excel find/replace

### Day 2 - June 19
- **Learned:** Window Functions in SQL (Rank, Row Number, Lag, Lead)

### Day 3 - June 20
- **Learned:** CTEs Queries

### Day 4-6 - June 21 to June 24
- **Learned:** SubQueries, Joins, CaseWhen, Having, Datefunctions
- **File:** `SQL_queries.sql`

### Day 7-8 June 25,26
- **Learned:** PYTHON- groupby, Aggregate, filtering, Merge
 PYTHON- Postgre connection, Data quality checks, date/time operations, string operations
- **File:** `Python_code.ipynb`

### Day 9-14 - June 27 to July 2
**Project 1: Pakistan Climate Analysis ETL**
- Worked with 3 CSV files (Global, Pakistan, Karachi) 
- CSV | Cleaning through Pandas | Load to Postgre | basic Insights with querys

**Project 2: PKR Exchange Rate ETL Pipeline**
- Fetched live JSON data from ExchangeRate-API
- Parsed and transformed 8 target currencies, calculated PKR equivalent rates
- Loaded to PostgreSQL with append mode to build historical data over time
- Secured API key and DB credentials using .env + python-dotenv
- Converted notebook to .py script, automated with Windows Task Scheduler (daily)


