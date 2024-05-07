-- SELECT seller_id FROM (
--     SELECT seller_id, RANK() OVER (ORDER BY SUM(price) DESC) as rk 
--     FROM Sales GROUP BY seller_id
-- )q1 WHERE q1.rk=1;

with cte_sales as(
select seller_id, sum(price) as total_sales
from sales 
group by seller_id
) 

select seller_id from cte_sales 
where total_sales = (select max(total_sales) from cte_sales)
