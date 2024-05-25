/* Write your T-SQL query statement below */

select department,employee, salary 
from 
(select d.name as department,e.name as employee,salary, rank() over (partition by d.name order by salary desc) rk from 
department d
left join 
employee e 
on e.departmentId = d.id)
a
where rk = 1
and employee is not null

