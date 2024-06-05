--CTE to create row numbers for all rows
WITH rownumPointCTE AS(
SELECT ROW_NUMBER() OVER(ORDER BY x,y) rn,x,y
FROM Point2D)

--join using row_number 
SELECT ROUND(CAST(MIN(SQRT(POWER((p2.x - p1.x),2) + POWER((p2.y - p1.y),2))) AS FLOAT),2) shortest
FROM rownumPointCTE p1
JOIN rownumPointCTE p2
ON p1.rn != p2.rn