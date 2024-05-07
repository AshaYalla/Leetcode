/* Write your T-SQL query statement below */


SELECT
    ROUND(
        coalesce(
            (SELECT
                CAST(
                    COUNT(DISTINCT CHECKSUM(requester_id, accepter_id)) 
                    AS FLOAT)
             FROM RequestAccepted)
            /
            (SELECT
                NULLIF(
                    COUNT(DISTINCT CHECKSUM(sender_id, send_to_id))
                    , 0.0)
             FROM FriendRequest)
        , 0.0)
    , 2) AS accept_rate