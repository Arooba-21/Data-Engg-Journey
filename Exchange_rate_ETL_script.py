#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
print(os.getcwd())


# In[3]:


from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")
print("Key loaded:", API_KEY is not None)


# In[4]:


import requests
from datetime import datetime

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

response = requests.get(url)
data = response.json()

print("Status:", data["result"])
print("Last updated:", data["time_last_update_utc"])
print("Total currencies:", len(data["conversion_rates"]))


# In[5]:


import pandas as pd
#filter the currencies you like or need not all 160+
target_currencies = ["PKR", "EUR", "GBP", "AED", "SAR", "CNY", "INR", "JPY"]

rates = data["conversion_rates"] 
#dict of data (k=key,v=value) 
filtered_rates = {k: v for k, v in rates.items() if k in target_currencies}

# DataFrame(dict into table)
df = pd.DataFrame(list(filtered_rates.items()), columns=["currency", "rate_vs_usd"])

# PKR value calculation
#storing pkr value in pkr_rate
pkr_rate = rates["PKR"]
#new columns
#for each currency rates according to pkr
df["rate_vs_pkr"] = (pkr_rate / df["rate_vs_usd"]).round(2)
#timestamp
df["fetched_at"] = datetime.now()
df["base_currency"] = "USD"

print(df)


# In[7]:


from sqlalchemy import create_engine
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(f"postgresql://postgres:{DB_PASSWORD}@localhost/Query_practice")

df.to_sql(
    "exchange_rates",
    engine,
    if_exists="append",
    index=False
)

print(f"✓ {len(df)} rows loaded at {datetime.now()}")


# In[ ]:




