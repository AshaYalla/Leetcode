/* Write your T-SQL query statement below */

with cte as (select contest_id,u.user_id,u.medal
    from contests 
    unpivot(user_id for medal in ([gold_medal],[silver_medal],[bronze_medal])) u),
cte2 as (
    select *, contest_id - rank() over (partition by user_id order by contest_id) as grouprk from cte
)
select name, mail from users u
left join(
select distinct user_id from cte2
group by user_id, grouprk
having count(grouprk) >= 3
union
select user_id
from cte2
where medal = 'gold_medal'
group by user_id
having count(user_id) >=3) t1
on t1.user_id = u.user_id
where t1.user_id is not null

