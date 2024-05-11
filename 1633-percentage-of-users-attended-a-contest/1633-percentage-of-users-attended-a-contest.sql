/* Write your T-SQL query statement below */

-- with cte_user as(
-- select count(distinct user_id) as usercount from Users
-- )

-- select distinct contest_id, round(count( user_id) over (partition by contest_id) * 100.0 / nullif((select usercount from cte_user),0),2) as percentage
-- from Register
-- order by percentage desc


select 
contest_id, 
round(count(distinct user_id) * 100.0 /(select count(user_id) from Users) ,2) as percentage
from  Register
group by contest_id
order by percentage desc,contest_id