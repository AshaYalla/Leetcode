/* Write your T-SQL query statement below */

select round(sum(iif( order_date = customer_pref_delivery_date,1,0)) * 100.0 / count(delivery_id) ,2)as immediate_percentage
from (select *, row_number() over (partition by customer_id order by order_date asc ) as rk from
Delivery 
 ) as imm
 where rk = 1
