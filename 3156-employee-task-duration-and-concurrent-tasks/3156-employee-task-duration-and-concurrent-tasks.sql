with cte as (
  select
    a.employee_id,
    a.task_id as base_task_id,
    b.task_id as pair_task_id,
    a.start_time as base_start_time,
    a.end_time as base_end_time,
    b.start_time as pair_start_time,
    b.end_time as pair_end_time
  from
    tasks as a
  inner join
    tasks as b
  on
    a.employee_id = b.employee_Id
    -- Find overlap and non-overlap itself
    and a.start_time <= b.start_time
    and b.start_time < a.end_time
    
),

-- Count concurrent tasks
cte2 as (
  select
    employee_id,
    -- If a task_id is equal to b task_id, it's not overlap job
    base_task_id,
    -- For each task, count how many count task IDs are overlapped
    -- It's 1 if not overlap
    count(pair_task_id) as concurrent_task_count
  from
    cte
  group by
    employee_id,
    base_task_id
),
cte3 as (
  select
    employee_id,
    max(concurrent_task_count) as max_concurrent_tasks
  from
    cte2
  group by
    employee_id
)
,

-- Duration
cte4 as (
  select
    employee_id,
    floor(sum(iif(
      base_task_id = pair_task_id,
      datediff(second, base_start_time, base_end_time),
      -datediff(second, pair_start_time, base_end_time)
    )) / 60 / 60) as total_task_hours
  from
    cte
  group by
    employee_id
)

select
  a.employee_id,
  a.total_task_hours,
  b.max_concurrent_tasks
from
  cte4 as a
left join
  cte3 as b
on
  a.employee_id = b.employee_id
order by
 a.employee_id


