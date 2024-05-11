/* Write your T-SQL query statement below */
Select left(order_date,7) as month,count(order_id) as order_count,
count(distinct customer_id) as customer_count
From Orders
Where invoice>20
Group By left(order_date,7)
