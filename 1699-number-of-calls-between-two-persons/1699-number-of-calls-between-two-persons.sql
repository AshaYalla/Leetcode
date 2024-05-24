/* Write your T-SQL query statement below */

select person1, person2, count(person1) as call_count, sum(duration) as total_duration
from (
select iif( from_id > to_id, to_id , from_id) as person1,
iif ( from_id > to_id, from_id, to_id) as person2,
duration
from calls) a
group by person1, person2