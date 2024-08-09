/* Write your T-SQL query statement below */

select username, activity, startDate, endDate from
(select *, count(activity) over(partition by username ) as totalactivities, 
rank() over(partition by username order by startDate desc) as activityrank
from UserActivity) a
where a.totalactivities = 1 or activityrank = 2