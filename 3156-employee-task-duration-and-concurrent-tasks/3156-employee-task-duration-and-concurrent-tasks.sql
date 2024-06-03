/* Write your T-SQL query statement below */
with consec_table as (
Select *,
datediff(minute,start_time,end_time) as total_work_hrs,
lead(start_time) over (partition by employee_id  order by start_time) as consec_end_time
from Tasks
),
overlap as (
Select employee_id,total_work_hrs, consec_end_time ,
case when consec_end_time is not null and end_time > consec_end_time
then datediff(minute,consec_end_time,end_time)
else null end as overlap
from consec_table
)
Select 
employee_id,
floor(sum(total_work_hrs)/60.0) as total_task_hours,
isnull(max(concurrent_tasks),1) as max_concurrent_tasks
from (
Select employee_id,
total_work_hrs = total_work_hrs  - isnull(overlap,0),
case when overlap is not null then 2 else null end as concurrent_tasks
from overlap
) X
group by employee_id