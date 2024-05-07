-- SELECT CAST(ISNULL(1.0 * 
--     (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) A)
--      / NULLIF((SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) R), 0)
--                    , 0)
--        AS DECIMAL(3,2)) AS accept_rate


select 
COALESCE(
CAST(
1.0*(SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) A)
/
NULLIF((SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) R),0)
as DECIMAL(3,2)),0.0) as accept_rate

-- https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/discuss/1513054/SQL-Server-2-Follow-up-Questions-sum()-over()-to-get-cumulative-sum