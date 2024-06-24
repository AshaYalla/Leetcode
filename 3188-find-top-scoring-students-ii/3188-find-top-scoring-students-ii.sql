/* Write your T-SQL query statement below */
with cte_major as(
select major, isnull(sum(case when mandatory = 'yes' then 1 end),0) as mandatorycount,
isnull(sum(case when mandatory = 'no' then 1 end),0) as electivecount
from courses
group by major
),

studentstats as (
select s.student_id, s.major,
isnull(sum(case when c.mandatory = 'yes' and s.major = c.major then 1 end),0) as studentmandatorycount,
isnull(sum(case when c.mandatory = 'no' and s.major = c.major then 1 end),0) as studentelectivecount,
isnull(sum(case when c.mandatory = 'yes' and s.major = c.major and e.grade <> 'A' then 1 end),0) as mandatoryfailgrade,
isnull(sum(case when c.mandatory = 'no' and s.major = c.major and (e.grade > 'B') then 1 end),0) as electivefailgrade,
iif(isnull(round(avg(e.gpa),2),0) >= 2.5,1,0) as avggpa
from students s
left join enrollments e 
on e.student_id = s.student_id
left join courses c
on c.course_id = e.course_id
group by s.student_id,s.major)



select distinct student_id
from studentstats s
left join cte_major m
on s.major = m.major


where avggpa = 1 and 
studentmandatorycount = mandatorycount
and studentelectivecount >=2
and mandatoryfailgrade < 1
and electivefailgrade < 1



