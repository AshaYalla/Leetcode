/* Write your T-SQL query statement below */

select actor_id, director_id from (select distinct actor_id, director_id, count(timestamp) as meetcount
from ActorDirector
group by actor_id, director_id) coord
where coord.meetcount >= 3