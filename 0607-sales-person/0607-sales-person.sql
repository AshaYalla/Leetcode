/* Write your T-SQL query statement below */

select name from SalesPerson
where name not in (
select distinct s.name from 
orders o
left join Company c
on o.com_id = c.com_id 
left join SalesPerson s
on o.sales_id = s.sales_id
where c.name = 'RED') 

