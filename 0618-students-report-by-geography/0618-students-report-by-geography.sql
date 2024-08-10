/* Write your T-SQL query statement below */
select min(America) as america ,min(Asia) as asia,min(Europe) as europe
from(
select 
    iif(Continent='America',Name,NULL)AS America,
    iif(Continent='Asia',Name,NULL)AS Asia,
    iif(Continent='Europe',Name,NULL) AS Europe,
   row_number() over(partition by continent order by name) As rn
from student
    ) t
group by rn