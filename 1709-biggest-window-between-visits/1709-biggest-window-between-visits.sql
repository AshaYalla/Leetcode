/* Write your T-SQL query statement below */

select user_id, max(biggest_window) biggest_window
from
(select user_id, datediff(day, visit_date, isnull(lead(visit_date) over( partition by user_id order by visit_date),'2021-1-1') ) biggest_window
from UserVisits)a

group by user_id

