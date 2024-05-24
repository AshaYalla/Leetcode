/* Write your T-SQL query statement below */

select top 1 requester_id id, count(*) num


from (select requester_id, accepter_id from RequestAccepted
union all
select accepter_id, requester_id from RequestAccepted) a

group by requester_id
order by count(*)  desc

-- with base as(select requester_id id from RequestAccepted
-- union all
-- select accepter_id id from RequestAccepted)


-- select id, count(*) num  from base group by 1 order by 2 desc limit 1