/* Write your T-SQL query statement below */


select sell_date, count(product) num_sold, STRING_AGG(product, ',') products
from (select distinct * from activities ) c 
group by sell_date


-- WITH t AS (SELECT DISTINCT * FROM Activities)

-- SELECT 
--     t.sell_date,
--     COUNT(t.product) AS num_sold,
--     STRING_AGG(t.product, ',') WITHIN GROUP (ORDER BY t.product) as products
-- FROM t
-- GROUP BY sell_date
-- ORDER BY sell_date