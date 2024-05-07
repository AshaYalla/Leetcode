/* Write your T-SQL query statement below */
with cte_sales as(
select seller_id, sum(price) as total_sales
from sales 
group by seller_id
) 

select seller_id from cte_sales 
where total_sales = (select max(total_sales) from cte_sales)

