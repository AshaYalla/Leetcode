/* Write your T-SQL query statement below */

select distinct p.product_id, coalesce(a.new_price, 10) as price from products p
left join 

(select product_id, new_price, row_number() over(partition by product_id order by change_date desc) as rk from products
where change_date <= '2019-08-16') a

on p.product_id = a.product_id and rk = 1
