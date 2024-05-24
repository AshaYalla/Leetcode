declare @allproducts int
select @allproducts =  count(distinct product_key) from Product

select customer_id 
from customer
group by customer_id
having count(distinct product_key) = @allproducts

