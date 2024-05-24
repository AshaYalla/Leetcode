# Write your MySQL query statement below
SELECT customer_id
FROM Customer c1
GROUP BY customer_id
HAVING COUNT(DISTINCT(c1.product_key)) = (
    SELECT COUNT(p.product_key) AS total_products_bought
    FROM Product p
)