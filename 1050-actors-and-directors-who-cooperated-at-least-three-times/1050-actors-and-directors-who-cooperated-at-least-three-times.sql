with cte_meet as (
    select actor_id, director_id,
    row_number() over (partition by actor_id, director_id order by timestamp ) rt
    from ActorDirector
    
)

select distinct actor_id, director_id from cte_meet
where rt>=3

