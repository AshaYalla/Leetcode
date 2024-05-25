SELECT player_id,player_name,
SUM(case when player_id=Wimbledon then 1 else 0 end) +
SUM(case when player_id=Fr_open then 1 else 0 end) +
SUM(case when player_id=US_open then 1 else 0 end) +
SUM(case when player_id=Au_open then 1 else 0 end)
as grand_slams_count
FROM Players
JOIN Championships
ON player_id  = Wimbledon
or player_id  = Fr_open 
or player_id  = US_open 
or player_id  = Au_open
GROUP BY player_id,player_name;