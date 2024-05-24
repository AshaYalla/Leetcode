/* Write your T-SQL query statement below */


select Department, Employee, Salary from (select d.name as department, e.name as Employee, salary, dense_rank() over (partition by departmentId order by salary desc) as rk
from employee e
left join 
 department d
 on d.id = e.departmentId
) salaryranking where salaryranking.rk <= 3


