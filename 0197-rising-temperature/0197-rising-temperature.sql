# Write your MySQL query statement below

# select w1.id from weather w1
# join weather w2
# on datediff(w1.recordDate, w2.recordDate) = 1
# where   w1.temperature > w2.temperature 

select id from
(select *, lag(recordDate, 1) over(order by recordDate asc) as prevdate,
lag(temperature,1 ) over(order by recordDate asc) as prevtemp
from weather)A 
where A.temperature > A.prevtemp and datediff(recordDate, prevdate) = 1


# select id from (
#     select *, lag(temperature,1) over(order by recordDate) as prevtemp, lag(recordDate,1) over(order by recordDate) as prevdate
# from weather) a
# where datediff(recordDate, prevdate) = 1 and temperature > prevtemp