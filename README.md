# Customer Shopping Behavior Analysis

An end-to-end data analysis project analyzing customer shopping patterns using Python, MySQL, and Power BI.

---

## 📌 Business Problem
A leading retail company wants to better understand its customers' shopping behavior to improve sales, customer satisfaction, and long-term loyalty. The goal is to uncover which factors — discounts, reviews, seasons, or payment preferences — drive consumer decisions and repeat purchases.

---

## 🛠️ Tech Stack
- **Python** — Data cleaning & transformation
- **MySQL** — Data storage & SQL analysis
- **Power BI** — Interactive dashboard
- **Libraries** — Pandas, NumPy, SQLAlchemy, Matplotlib, Seaborn

---

## 📁 Project Structure

customer-shopping-analysis/

├── data/                        → Raw dataset

├── notebooks/                   → Jupyter notebook (EDA)

├── src/

│   ├── db_connection.py         → MySQL connection helper

│   └── analysis.py              → ETL pipeline

├── dashboard/                   → Power BI dashboard (.pbix)

├── customer_behavior_sql_queries.sql  → 10 SQL business queries

├── Customer Shopping Behavior Analysis.pdf  → Project report

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
git clone https://github.com/yourusername/customer-shopping-analysis.git
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

**4. Configure MySQL**
Create a `.env` file in the root folder:
DB_USERNAME=root

DB_PASSWORD=your_password

DB_HOST=localhost

DB_PORT=3306

DB_NAME=customer_behavior

**5. Create MySQL database**
```sql
CREATE DATABASE customer_behavior;
```

**6. Run the pipeline**
```bash
python src/analysis.py
```

---

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

## 💡 Key Insights
- **Male customers** generate significantly higher revenue ($157,890) than female ($75,191)
- **73% of customers** are non-subscribers but contribute the majority of revenue
- **Young Adults** are the highest revenue-generating age group ($62,143)
- **Loyal customers** make up 80% of the customer base (3,116 out of 3,900)
- **Express shipping** users have a slightly higher average spend ($60.48) vs Standard ($58.46)

---

## ✅ Business Recommendations
- **Boost Subscriptions** — Promote exclusive benefits to convert 73% non-subscribers
- **Loyalty Program** — Reward repeat buyers to retain 3,116 loyal customers
- **Target Young Adults** — Focus marketing on highest revenue age group
- **Review Discount Policy** — 50% of Hat purchases use discounts; balance margin vs sales
- **Product Campaigns** — Highlight Gloves, Sandals, Boots (highest rated products)