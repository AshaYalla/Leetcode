WITH add_rank AS
    (SELECT id, company, salary,
        ROW_NUMBER()OVER(PARTITION BY company ORDER BY salary) AS rnk
    FROM Employee)
, add_count AS
    (SELECT company, COUNT(DISTINCT id) AS cnt
    FROM Employee
    GROUP BY company)
SELECT a.id, a.company, a.salary
FROM add_rank a
JOIN add_count b
ON a.company = b.company
AND a.rnk BETWEEN b.cnt*1.0 / 2 AND b.cnt / 2 + 1