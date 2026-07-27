-- ============================================================
-- DATA CLEANING - Customer Shopping Behavior
-- ============================================================

-- Step 1: Check raw data
RENAME TABLE customer TO customer_raw;

SELECT * FROM customer_raw LIMIT 5;

-- Step 2: Check total records
SELECT COUNT(*) AS total_records FROM customer_raw;

-- Step 3: Check missing values
SELECT 
    SUM(CASE WHEN `Review Rating` IS NULL THEN 1 ELSE 0 END) AS missing_review_rating,
    SUM(CASE WHEN `Purchase Amount (USD)` IS NULL THEN 1 ELSE 0 END) AS missing_purchase_amount,
    SUM(CASE WHEN Gender IS NULL THEN 1 ELSE 0 END) AS missing_gender,
    SUM(CASE WHEN Age IS NULL THEN 1 ELSE 0 END) AS missing_age
FROM customer_raw;

-- Step 4: Check duplicates
SELECT `Customer ID`, COUNT(*) 
FROM customer_raw
GROUP BY `Customer ID`
HAVING COUNT(*) > 1;

-- Step 5: Create cleaned table with renamed columns
CREATE TABLE customer AS
SELECT 
    `Customer ID`            AS customer_id,
    Age                      AS age,
    Gender                   AS gender,
    `Item Purchased`         AS item_purchased,
    Category                 AS category,
    `Purchase Amount (USD)`  AS purchase_amount,
    Location                 AS location,
    Size                     AS size,
    Color                    AS color,
    Season                   AS season,
    `Review Rating`          AS review_rating,
    `Subscription Status`    AS subscription_status,
    `Shipping Type`          AS shipping_type,
    `Discount Applied`       AS discount_applied,
    `Previous Purchases`     AS previous_purchases,
    `Payment Method`         AS payment_method,
    `Frequency of Purchases` AS frequency_of_purchases
FROM customer_raw;

-- Step 6: Handle missing values in review_rating
UPDATE customer c1
SET review_rating = (
    SELECT AVG(c2.review_rating)
    FROM (SELECT * FROM customer) c2
    WHERE c2.category = c1.category
    AND c2.review_rating IS NOT NULL
)
WHERE review_rating IS NULL;

-- Step 7: Add age_group column
ALTER TABLE customer ADD COLUMN age_group VARCHAR(20);

UPDATE customer
SET age_group = CASE
    WHEN age BETWEEN 18 AND 31 THEN 'Young Adult'
    WHEN age BETWEEN 32 AND 44 THEN 'Adult'
    WHEN age BETWEEN 45 AND 57 THEN 'Middle-aged'
    ELSE 'Senior'
END;

-- Step 8: Add purchase_frequency_days column
ALTER TABLE customer ADD COLUMN purchase_frequency_days INT;

UPDATE customer
SET purchase_frequency_days = CASE
    WHEN frequency_of_purchases = 'Weekly'         THEN 7
    WHEN frequency_of_purchases = 'Fortnightly'    THEN 14
    WHEN frequency_of_purchases = 'Bi-Weekly'      THEN 14
    WHEN frequency_of_purchases = 'Monthly'        THEN 30
    WHEN frequency_of_purchases = 'Quarterly'      THEN 90
    WHEN frequency_of_purchases = 'Every 3 Months' THEN 90
    WHEN frequency_of_purchases = 'Annually'       THEN 365
END;

-- Step 9: Verify cleaned data
SELECT * FROM customer LIMIT 5;

-- Step 10: Verify new columns
SELECT DISTINCT age_group FROM customer;
SELECT DISTINCT purchase_frequency_days FROM customer;

-- Step 11: Final record count
SELECT COUNT(*) AS total_cleaned_records FROM customer;