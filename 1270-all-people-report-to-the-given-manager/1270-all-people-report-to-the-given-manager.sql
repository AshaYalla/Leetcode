with cte as (

select employee_id, 1 as rank from employees
    where manager_id = 1
union all
    
select  e.employee_id, rank + 1 from employees e
join cte c
on manager_id = c.employee_id
where rank < 4
    

)

select distinct employee_id from cte
where employee_id <> 1