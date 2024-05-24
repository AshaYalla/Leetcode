/* Write your T-SQL query statement below */

select student_id, course_id, grade from
(select *,row_number() over (partition by student_id order by grade desc, course_id asc) rk
from enrollments
) a
where rk = 1