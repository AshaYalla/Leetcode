select project_id,round(avg(cast(experience_years as decimal(10,2))),2) as average_years from Project a
join Employee b
on a.employee_id=b.employee_id
group by project_id
order by project_id 