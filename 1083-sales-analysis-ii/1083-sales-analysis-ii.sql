/* Write your T-SQL query statement below */


SELECT DISTINCT s.buyer_id
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id
AND p.product_name = 'S8'
LEFT JOIN
    (
    SELECT DISTINCT buyer_id
    FROM Sales s
    JOIN Product p
    ON s.product_id = p.product_id
    AND p.product_name = 'iPhone'
    )a
ON s.buyer_id = a.buyer_id
WHERE a.buyer_id IS NULL

-- select distinct buyer_id from sales s
-- left join 
-- product p 
-- ON p.product_id = s.product_id
-- where p.product_name = 'S8'
-- and buyer_id not in (
    
--     SELECT DISTINCT buyer_id
-- FROM Sales s
-- JOIN Product p
-- ON s.product_id = p.product_id
-- where p.product_name = 'iPhone'

-- )
