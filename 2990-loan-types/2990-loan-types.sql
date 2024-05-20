SELECT user_id
FROM loans
GROUP BY user_id
HAVING SUM(CASE WHEN loan_type = 'Refinance' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN loan_type = 'Mortgage' THEN 1 ELSE 0 END) > 0
ORDER BY user_id ASC;

-- SELECT user_id
-- FROM Loans
-- WHERE loan_type IN ('Refinance', 'Mortgage')
-- GROUP BY user_id
-- HAVING COUNT(DISTINCT loan_type) = 2
-- ORDER BY user_id;