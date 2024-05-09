# Write your MySQL query statement below
# select player_id, min(event_date) as first_login  from activity 
# group by player_id


select player_id, event_date as first_login from 
(select player_id, event_date, row_number() over(PARTITION BY player_id ORDER BY event_date asc) loginorder
from activity) l
where loginorder = 1
