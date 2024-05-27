/* Write your T-SQL query statement below */

select period_state, min(taskdate) start_date, max(taskdate) end_date
from
(select fail_date as taskdate, 'failed' as period_state,
 dateadd(day, row_number() over ( order by fail_date desc ), fail_date) as groupdate
 
 from Failed
where year(fail_date) = 2019
union 
select success_date as taskdate, 'succeeded' as period_state,
 dateadd(day, row_number() over ( order by success_date desc ), success_date) as groupdate
 from Succeeded
where year(success_date) = 2019) a
group by groupdate, period_state
order by start_date

