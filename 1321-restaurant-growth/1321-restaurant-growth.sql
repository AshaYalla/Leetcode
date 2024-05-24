/* Write your T-SQL query statement below */

with cte_table as (select visited_on, sum(amount) as amount
from Customer 
group by visited_on)

select visited_on, 
sum(amount) over(order by visited_on rows between 6 preceding and CURRENT ROW) as amount,
round(avg(amount *1.0) over(order by visited_on rows between 6 preceding and CURRENT ROW),2) as average_amount
from cte_table
order by visited_on
OFFSET 6 ROWS;
