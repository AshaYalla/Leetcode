# Write your MySQL query statement below

select extra as report_reason, count(DISTINCT post_id) as report_count
from actions
where action = 'report' and action_date = '2019-07-04'

group by extra
