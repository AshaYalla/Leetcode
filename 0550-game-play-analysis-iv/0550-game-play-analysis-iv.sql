/* Write your T-SQL query statement below */

with cte_table as (
select *, row_number() over (partition by player_id order by event_date) as rk
    
    from Activity
)

select round(count(distinct b.player_id) * 1.0 / count(distinct a.player_id),2) as fraction 
from cte_table a
left join cte_table b 
on datediff(day,a.event_date, b.event_date) = 1 and a.player_id = b.player_id
and a.event_date != b.event_date
and b.player_id is not null
where a.rk = 1

