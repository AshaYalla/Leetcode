/* Write your T-SQL query statement below */

select  distinct a.student_name as member_A, 
        b.student_name as member_B, 
        c.student_name as member_C 
from schoolA as a 
join schoolB as b on a.student_id != b.student_id 
                                       and a.student_name != b.student_name
join schoolC as c on c.student_id ! = b.student_id  and c.student_name != b.student_name
and c.student_name != a.student_name and  c.student_id != a.student_id