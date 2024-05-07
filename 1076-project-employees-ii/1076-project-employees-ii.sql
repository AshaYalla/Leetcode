

DECLARE @MaxProjectCount INT = (SELECT TOP 1 COUNT(*) as count_of_employee FROM Project GROUP BY project_id ORDER BY count_of_employee DESC)

SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(*) = @MaxProjectCount
