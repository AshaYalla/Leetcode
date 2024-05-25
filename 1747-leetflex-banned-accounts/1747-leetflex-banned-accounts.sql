/* Write your T-SQL query statement below */

SELECT
  distinct l1.account_id
FROM
  LogInfo l1
CROSS JOIN
  LogInfo l2
 where l1.account_id = l2.account_id
 and l1.ip_address != l2.ip_address
 and l1.login <= l2.logout and l1.login >= l2.login