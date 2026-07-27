"""
load_data.py
------------
Loads raw CSV data into MySQL customer_behavior database as customer_raw table.
Run data_cleaning.sql after this to create the cleaned customer table.
"""

import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# MySQL connection
username = "root"
password = quote_plus("mysql@SUKH9")
host     = "localhost"
port     = "3306"
database = "customer_behavior"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Load raw CSV into MySQL
df = pd.read_csv("data/customer_shopping_behavior.csv")
df.to_sql("customer_raw", engine, if_exists="replace", index=False)
print(f"✅ {len(df)} raw records loaded into customer_raw table successfully!")