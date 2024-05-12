with cte(dt, customer_id, transaction_date, start_date, amount) as 
         (select 1 dt, 
                 t.customer_id customer_id,
                 t.transaction_date transaction_date, 
                 t.transaction_date start_date,
                 t.amount amount
            from Transactions t
           where not exists (select 1
                               from Transactions p
                              where p.customer_id = t.customer_id 
                                and DateAdd(day, 1, p.transaction_date) = t.transaction_date
                                and p.amount < t.amount)
           union all 

          select c.dt + 1 dt,
                 t.customer_id as customer_id,
                 t.transaction_date as transaction_date,
                 c.start_date as start_date,
                 t.amount as amount
            from Transactions t join
                 cte c on (c.customer_id = t.customer_id 
                       and DateAdd(day, 1, c.transaction_date) = t.transaction_date
                       and t.amount > c.amount) 
)

  select customer_id, 
         start_date consecutive_start,
         DateAdd(day, Max(dt) - 1, start_date) consecutive_end
    from cte
group by customer_id, 
         start_date 
  having Max(dt) >= 3
order by customer_id,
         start_date
