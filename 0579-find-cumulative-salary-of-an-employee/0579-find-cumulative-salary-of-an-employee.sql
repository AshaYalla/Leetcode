/* Write your T-SQL query statement below */

with cte_employee as 
(
    select * from (
select id, month, salary, rank() over (partition by id order by month desc) rk
from employee
)a
where rk > 1
)

select c1.id,c1.month, sum(c2.salary) as Salary from cte_employee c1
left join cte_employee c2
on c1.id = c2.id and c1.month - c2.month in (0,1,2)
group by c1.id,c1.month
order by c1.id asc, c1.month desc

