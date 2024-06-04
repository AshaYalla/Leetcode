/* Write your T-SQL query statement below */
SELECT distinct transaction_id
FROM (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY convert(date, day) ORDER BY amount DESC) AS rnk
    FROM Transactions
) AS t
WHERE rnk = 1
ORDER by 1;

