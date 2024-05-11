/* Write your T-SQL query statement below */

select distinct c1.user_id from 
confirmations c1 
left join confirmations c2
on c1.user_id = c2.user_id 
and DATEDIFF(ss,c1.time_stamp,c2.time_stamp) > 0 and DATEDIFF(SS, c1.time_stamp, c2.time_stamp) <= 86400
where c2.user_id is not null
-- where c2.user_id is not null
-- and DATEDIFF(ss,c1.time_stamp,c2.time_stamp) <= 86400

-- select distinct
-- 	c1.user_id
-- from dbo.confirmations as c1

-- cross join dbo.confirmations as c2

-- where c1.user_id = c2.user_id
-- and DATEDIFF(ss,c1.time_stamp,c2.time_stamp) > 0
-- and DATEDIFF(ss,c1.time_stamp,c2.time_stamp) <= 86400