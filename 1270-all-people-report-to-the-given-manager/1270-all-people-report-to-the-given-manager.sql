/* Write your T-SQL query statement below */
select a.employee_id
from Employees a, Employees b, Employees c
where a.employee_id <> 1 and a.manager_id = b.employee_id and b.manager_id = c.employee_id and (b.manager_id = 1 or c.manager_id = 1)