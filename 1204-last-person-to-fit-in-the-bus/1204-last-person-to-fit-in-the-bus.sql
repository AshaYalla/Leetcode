/* Write your T-SQL query statement below */


select top 1 person_name from
(select *, sum(weight) over(order by turn) as runningweight  from Queue) a
where runningweight <= 1000
order by runningweight desc
