/* Write your T-SQL query statement below */
-- select bin, total from (
--     select sum( case when duration < 300 then 1 end) as '[0-5>',
-- sum(CASE WHEN (duration/60 >= 5) AND (duration/60 < 10) THEN 1 END) AS '[5-10>',
-- isnull(sum(CASE WHEN (duration/60 >= 10) AND (duration/60 < 15) THEN 1 END) ,0)AS '[10-15>',
-- sum(CASE WHEN (duration/60 >= 15) THEN 1 END) AS '15 or more'
-- from Sessions) as pvt

-- unpivot
--     (total FOR bin IN ("[0-5>","[5-10>","[10-15>","15 or more")) AS unpvt

SELECT bin, total
FROM 
(SELECT
COUNT(CASE WHEN (duration/60 < 5) THEN 1 END) AS '[0-5>',
COUNT(CASE WHEN (duration/60 >= 5) AND (duration/60 < 10) THEN 1 END) AS '[5-10>',
COUNT(CASE WHEN (duration/60 >= 10) AND (duration/60 < 15) THEN 1 END) AS '[10-15>',
COUNT(CASE WHEN (duration/60 >= 15) THEN 1 END) AS '15 or more'
FROM Sessions) as pivoted_tbl
UNPIVOT
    (total FOR bin IN ("[0-5>","[5-10>","[10-15>","15 or more")) AS unpvt;