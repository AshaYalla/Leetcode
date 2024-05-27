with cte as (
    select month(join_date) month,
           year(join_date) year,
           sum(count(driver_id)) over (
                        order by year(join_date),month(join_date)
            ) as cs
    from Drivers
    where year(join_date) <= 2020
    group by year(join_date), month(join_date)
),
cte1 as (
    select month(r.requested_at) month,
            count(r.ride_id) as accepted_rides
    from Rides r 
    join AcceptedRides ar 
        on r.ride_id = ar.ride_id
    where year(r.requested_at) = 2020
    group by month(r.requested_at)
)
select TableMonth.month
        , isnull(isnull(c.cs, max(c.cs)
                over (order by TableMonth.month)
            ),0) as active_drivers
        , isnull(c1.accepted_rides,0) accepted_rides
From (VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12)) 
AS TableMonth (month)
left join cte c 
    on TableMonth.month = c.month
    and c.year = 2020
left join cte1 c1 
    on TableMonth.month = c1.month

-- with monthcte as (
-- select 1 as month
-- union all 
-- select month + 1 from monthcte
-- where month < 12
-- ),
-- driverpermonth as (
--     select drivermonth,sum(drivercnt) as drivercnt from(
--     select case when year(join_date) < 2020 then 1 
--     else month(join_date)
--     end as drivermonth,
--     count(driver_id) as drivercnt
--     from drivers
--     where year(join_date)<= 2020
--     group by month(join_date), year(join_date)) a
--     group by drivermonth
-- ),
-- accepted as (
-- select month(requested_at) as month, count(driver_id) as accepted_rides
-- from rides r 
-- left join acceptedrides ar
-- on r.ride_id = ar.ride_id
-- and year(requested_at) = 2020
-- group by month(requested_at)
-- )

-- select m.month, 
-- isnull( sum(drivercnt) over (order by m.month),0) as active_drivers,
-- isnull(a.accepted_rides,0) as accepted_rides
-- from monthcte m
-- left join driverpermonth d
-- on d.drivermonth = m.month
-- left join accepted a
-- on a.month = m.month
