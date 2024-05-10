# Write your MySQL query statement below

select s.sub_id as post_id, coalesce(number_of_comments, 0) as number_of_comments from Submissions s
left join 
(select parent_id as post_id, count(distinct sub_id) as number_of_comments from submissions
where parent_id is not null
group by parent_id) pc

on pc.post_id = s.sub_id

where s.parent_id is null
group by s.sub_id
order by s.sub_id
