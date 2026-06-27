"""
analysis.py
-----------
Customer Shopping Behavior Analysis — loads, cleans, and pushes data to MySQL.
"""

import pandas as pd
from src.db_connection import get_engine


# ── 1. Load ──────────────────────────────────────────────────────────────────
df = pd.read_csv("data/customer_shopping_behavior.csv")
print("Shape:", df.shape)
print(df.head())

# ── 2. Inspect ───────────────────────────────────────────────────────────────
print(df.info())
print(df.describe(include="all"))
print("\nMissing values:\n", df.isnull().sum())

# ── 3. Clean ─────────────────────────────────────────────────────────────────
# Impute missing Review Rating with category median
df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(
    lambda x: x.fillna(x.median())
)

# Rename columns to snake_case
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.rename(columns={"purchase_amount_(usd)": "purchase_amount"})

# ── 4. Feature Engineering ───────────────────────────────────────────────────
# Age group
labels = ["Young Adult", "Adult", "Middle-aged", "Senior"]
df["age_group"] = pd.qcut(df["age"], q=4, labels=labels)

# Purchase frequency in days
frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Annually": 365,
    "Every 3 Months": 90,
}
df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)

# Drop redundant column
if "promo_code_used" in df.columns:
    df = df.drop("promo_code_used", axis=1)

print("\nFinal columns:", df.columns.tolist())

# ── 5. Push to MySQL ─────────────────────────────────────────────────────────
engine = get_engine()
table_name = "customer"

df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"\n✅ Data loaded into MySQL table '{table_name}'.")

# ── 6. Verify ────────────────────────────────────────────────────────────────
sample = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5;", engine)
print(sample)