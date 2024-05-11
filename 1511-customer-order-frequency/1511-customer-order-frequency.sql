# Write your MySQL query statement below


select customer_id, name
from
(select o.customer_id, name,  month(order_date) as month,sum(quantity * price) as summ from Orders o
join Product p 
on p.product_id = o.product_id
join Customers c 
on c.customer_id = o.customer_id
where year(order_date) = 2020 and (month(order_date) = 6 or month(order_date) = 7)
group by o.customer_id, month(order_date)) C
where summ >= 100  
group by customer_id, name
having count(month) = 2

