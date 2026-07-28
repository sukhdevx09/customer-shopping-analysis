"""
load_data.py
------------
Loads raw CSV data into MySQL customer_behavior database as customer_raw table.
Run data_cleaning.sql after this to create the cleaned customer table.
"""

import os
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
host     = os.getenv("DB_HOST")
port     = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

df = pd.read_csv("data/customer_shopping_behavior.csv")
df.to_sql("customer_raw", engine, if_exists="replace", index=False)
print(f"✅ {len(df)} raw records loaded into customer_raw table successfully!")