/* Write your T-SQL query statement below */

select a.sale_date, a.sold_num - coalesce(o.sold_num,0)  as diff  
from sales a
left join sales o
on a.sale_date = o.sale_date and 
o.fruit = 'oranges'
where a.fruit = 'apples'
  
