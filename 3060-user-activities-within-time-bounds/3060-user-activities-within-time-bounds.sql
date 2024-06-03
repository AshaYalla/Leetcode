/* Write your T-SQL query statement below */

select distinct s1.user_id
from sessions s1
left join sessions s2
on s1.user_id = s2.user_id and
s2.session_start <= dateadd(hour,12,s1.session_end)
and s2.session_start > s1.session_start
and s1.session_type = s2.session_type
and s1.session_id <> s2.session_id
where s2.session_start is not null


-- with CTE 
-- AS
-- (
-- select user_id, session_start, session_end, session_type, row_number()over(partition by user_id order by session_start ) as RN
-- from Sessions 
-- )
-- select distinct s1.user_id
-- from CTE s1
-- join CTE s2 
-- on s1.user_id = s2.user_id 
-- and s1.RN < s2.RN
-- and s1.session_type = s2.session_type 
-- and DATEADD(hour, 12, s1.session_end) >= s2.session_start