with a as ( 
select project_id
, count(employee_id)cnt
from project

group by project_id)

select project_id 
from a
where cnt = (select max(cnt)from a)
