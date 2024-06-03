with cte as (
    SELECT 
        SUBSTRING(tweet,CHARINDEX('#', tweet),len(tweet)) StringFrom#,
        len(SUBSTRING(tweet,CHARINDEX('#', tweet),len(tweet))) LenFrom#
    FROM Tweets
),
CTE1 AS (
    SELECT 
        LEFT(
            StringFrom#, 
                CASE WHEN CHARINDEX(' ',StringFrom#) = 0 THEN LenFrom# ELSE CHARINDEX(' ',StringFrom#) END
        ) AS hashtag
    from cte
)
SELECT TOP 3
    hashtag,
    COUNT(hashtag) AS HASHTAG_COUNT
FROM CTE1
GROUP BY hashtag
ORDER BY COUNT(hashtag) DESC, hashtag desc
