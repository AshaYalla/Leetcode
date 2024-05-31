/* Write your T-SQL query statement below */

with cte_humancount as (
select *, id - row_number() over (order by id) as groupid
from stadium 
where people >= 100
    ) 

select id, visit_date, people from cte_humancount
where groupid in (
select groupid from cte_humancount
group by groupid
having count(groupid) >= 3)