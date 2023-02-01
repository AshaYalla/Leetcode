/* Write your T-SQL query statement below */

select(select  distinct salary from (select *,DENSE_RANK() OVER (order by salary desc) as salaryrank
from Employee) p
where p.salaryrank = 2) as SecondHighestSalary


