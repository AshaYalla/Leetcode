/* Write your T-SQL query statement below */

-- select  distinct a.student_name as member_A, 
--         b.student_name as member_B, 
--         c.student_name as member_C 
-- from schoolA as a 
-- join schoolB as b on a.student_id != b.student_id 
--                                        and a.student_name != b.student_name
-- join schoolC as c on c.student_id ! = b.student_id  and c.student_name != b.student_name
-- and c.student_name != a.student_name and  c.student_id != a.student_id


SELECT member_A, member_B, member_C 
FROM (
SELECT A.student_id id_A, A.student_name member_A, B.student_id id_b, B.student_name member_B, C.student_id id_C, C.student_name member_C
FROM SchoolA A, SchoolB B, SchoolC C
) Schools
WHERE member_A <> member_B AND member_B <> member_C AND member_A <> member_C
AND id_A <> id_B AND id_B <> id_C AND id_A <> id_C