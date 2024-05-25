/* Write your T-SQL query statement below */

with cte as (
select log_id, row_number() over(order by log_id) - log_id as groupid
from logs)

select min(log_id) start_id, max(log_id) end_id
from cte 
group by groupid
order by groupid desc

