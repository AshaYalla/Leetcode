/* Write your T-SQL query statement below */
-- SELECT user_id, MAX(time_stamp) AS last_stamp
-- FROM Logins
-- WHERE YEAR(time_stamp) = 2020
-- GROUP BY user_id

select
    user_id, time_stamp as last_stamp
from (
    select 
        *,
        r = row_number() over (partition by user_id order by time_stamp desc) 
    from 
        logins 
    where year(time_stamp) = 2020
) sub
where sub.r = 1
