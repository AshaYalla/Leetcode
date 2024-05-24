/* Write your T-SQL query statement below */

select id, coalesce (iif(id% 2 = 0, lagstudent, leadstudent), student) as student
from (
    
select id, student, lead(student) over (order by id) as leadstudent, 
lag(student) over (order by id) as lagstudent
from seat


) a