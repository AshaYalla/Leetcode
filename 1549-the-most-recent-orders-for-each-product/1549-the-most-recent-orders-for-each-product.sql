/* Write your T-SQL query statement below */

select  product_name , product_id, order_id, order_date from 

(select  p.product_name , p.product_id, order_id, order_date , rank() over (partition by p.product_id order by order_date desc) as rk from products p 
left join orders o 
on o.product_id = p.product_id) 
a 
where rk = 1
and order_id is not null
order by 
product_name asc,
 product_id asc, order_id asc
