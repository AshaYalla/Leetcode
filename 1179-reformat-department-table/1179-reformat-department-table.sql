
SELECT
    *
FROM (SELECT id, 
             revenue, 
             CONCAT(month,'_Revenue') AS month
     FROM department) d
PIVOT(
    SUM(revenue)
    FOR month in ([Jan_Revenue],[Feb_Revenue],[Mar_Revenue],
                  [Apr_Revenue],[May_Revenue],[Jun_Revenue],
                  [Jul_Revenue],[Aug_Revenue],[Sep_Revenue],
                  [Oct_Revenue],[Nov_Revenue],[Dec_Revenue])
) AS P