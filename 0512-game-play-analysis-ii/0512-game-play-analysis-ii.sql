# Write your MySQL query statement below




select player_id, device_id  from 
(select player_id, event_date, device_id, row_number() over(PARTITION BY player_id ORDER BY event_date asc) loginorder
from activity) l
where loginorder = 1