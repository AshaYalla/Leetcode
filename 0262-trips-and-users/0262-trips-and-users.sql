select request_at Day, 
	cast(sum(iif(status in ('cancelled_by_driver', 'cancelled_by_client'), 1, 0))/ CAST(count(*) AS DECIMAL (9,2)) AS DECIMAL(9,2)) as [Cancellation Rate]
from Trips T, Users U1, Users U2
where T.client_id = U1.users_id and T.driver_id = U2.users_id
and U1.banned = 'No' and U1.role = 'client' and U2.banned = 'No' and U2.role = 'driver'
group by request_at
having request_at >= '2013-10-01' and request_at <= '2013-10-03'