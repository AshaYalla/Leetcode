/* Write your T-SQL query statement below */

select distinct C.country_name,

case when ISNULL (avg(W.weather_state * 1.0) over(partition by C.country_id) ,0) <= 15 then 'Cold'
when ISNULL (avg(W.weather_state) over(partition by C.country_id) ,0) >= 25 then 'Hot'
else 'Warm'

end as weather_type

from countries C
left join weather W 
on C.country_id = W.country_id
and month(day) = 11 and year(day) = 2019
where W.country_id is not null
