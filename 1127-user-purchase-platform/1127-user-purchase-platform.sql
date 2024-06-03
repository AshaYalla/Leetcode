with t as(
select distinct spend_date, 'mobile' as platform from Spending
union
select distinct spend_date, 'desktop' as platform from Spending
union
select distinct spend_date, 'both' as platform from Spending)


select t.spend_date, t.platform, 
isnull(sum(amount),0) as total_amount, 
isnull(count(distinct user_id),0) as total_users
from t
left join
(
    select spend_date, case when cnt = 2 then 'both' else platform end as platform, 
    user_id, amount, cnt
from
(select spend_date, platform, user_id, amount,
 count(platform)over(partition by spend_date, user_id) as cnt
from Spending) t3) t4
on t4.spend_date = t.spend_date and t.platform = t4.platform
group by t.spend_date, t.platform


