/* Write your T-SQL query statement below */

with cte as(
select task_id, 1 as subtask_id from Tasks
union all
select c.task_id, c.subtask_id + 1
from cte c
join tasks t
on t.task_id = c.task_id
where subtask_id < subtasks_count 

)

select * from cte
except 
select * from Executed