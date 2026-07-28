# Customer Shopping Behavior Analysis

An end-to-end data analysis project analyzing customer shopping patterns using Python, MySQL, and Power BI.

---

## 📌 Business Problem
A leading retail company wants to better understand its customers' shopping behavior to improve sales, customer satisfaction, and long-term loyalty. The goal is to uncover which factors — discounts, reviews, seasons, or payment preferences — drive consumer decisions and repeat purchases.

---

## 🛠️ Tech Stack
- **Python** — Loads raw data into MySQL
- **MySQL** — Data cleaning, feature engineering & business analysis (SQL)
- **Power BI** — Interactive dashboard
- **Libraries** — Pandas, SQLAlchemy, PyMySQL, python-dotenv

---

## 📁 Project Structure

customer-shopping-analysis/
├── data/ → Raw dataset (CSV)
├── src/
│ └── load_data.py → Loads raw CSV into MySQL as customer_raw
├── sql/
│ ├── data_cleaning.sql → Cleaning, dedup, missing values, feature engineering
│ └── business_queries.sql → 10 SQL business queries
├── deshboard/
│ ├── customer_behavior_deshboard.pbix → Power BI dashboard (source file)
│ └── customer_behavior_dashboard.pdf → Dashboard export (quick preview)
├── Customer Shopping Behavior Analysis.pdf → Project report
├── requirements.txt
└── README.md

---

## 📊 Dataset Summary
- **Rows:** 3,900
- **Columns:** 18
- **Key Features:** Age, Gender, Category, Purchase Amount, Season, Subscription Status, Review Rating, Shipping Type

---

## ⚙️ Setup Instructions

**1. Clone the repository**
```bash
git clone https://github.com/sukhdevx09/customer-shopping-analysis.git
cd customer-shopping-analysis
```

**2. Create virtual environment**
```bash
python -m venv p3venv
p3venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file** in the project root with your MySQL credentials:

DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=customer_behavior

**5. Create MySQL database**
```sql
CREATE DATABASE customer_behavior;
```

**6. Load raw data into MySQL**
```bash
python src/load_data.py
```

**7. Run SQL files in order**
- First run `sql/data_cleaning.sql`
- Then run `sql/business_queries.sql`

---

## 🧹 Data Cleaning & Feature Engineering (SQL)
- Renamed raw table to `customer_raw`, created a cleaned `customer` table with snake_case columns
- Checked total records, missing values, and duplicate customer IDs
- Imputed missing `review_rating` values using the average rating within the same product category
- Dropped `promo_code_used` (found identical to `discount_applied`)
- Added `age_group` column (Young Adult, Adult, Middle-aged, Senior)
- Added `purchase_frequency_days` column (converted from text frequency labels to numeric days)

## 🔍 SQL Analysis (10 Business Queries)
| # | Query | Technique |
|---|---|---|
| Q1 | Revenue by Gender | GROUP BY, SUM |
| Q2 | High-Spending Discount Users | Subquery |
| Q3 | Top 5 Products by Rating | GROUP BY, ORDER BY |
| Q4 | Standard vs Express Shipping | WHERE, AVG |
| Q5 | Subscribers vs Non-Subscribers | GROUP BY, ROUND |
| Q6 | Discount-Dependent Products | CASE WHEN |
| Q7 | Customer Segmentation | CTE |
| Q8 | Top 3 Products per Category | Window Function (ROW_NUMBER) |
| Q9 | Repeat Buyers & Subscriptions | WHERE, GROUP BY |
| Q10 | Revenue by Age Group | GROUP BY, SUM |

---

## 📈 Power BI Dashboard
Built on top of the 10 SQL queries — includes KPI cards (total customers, average review rating, average purchase amount), a subscription status breakdown, revenue/sales by category, revenue by age group, and slicers for gender and shipping type.

---

## 💡 Key Insights
- **Male customers** generate significantly higher revenue ($157,890) vs female ($75,191)
- **73% of customers** are non-subscribers but contribute majority of revenue
- **Young Adults** are the highest revenue-generating age group ($62,143)
- **Loyal customers** make up 80% of the customer base (3,116 out of 3,900)
- **Express shipping** users have slightly higher avg spend ($60.48) vs Standard ($58.46)

---

## ✅ Business Recommendations
- **Boost Subscriptions** — Promote exclusive benefits to convert 73% non-subscribers
- **Loyalty Program** — Reward repeat buyers to retain 3,116 loyal customers
- **Target Young Adults** — Focus marketing on highest revenue age group
- **Review Discount Policy** — 50% of Hat purchases use discounts; balance margin vs sales
- **Product Campaigns** — Highlight Gloves, Sandals, Boots (highest rated products)