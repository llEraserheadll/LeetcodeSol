-- select e.employee_id,e.name,count(m.reports_to) as reports_count,round(avg(m.age)) as average_age 
-- from Employees e 
-- inner join Employees m 
-- on e.employee_id = m.reports_to 
-- group by e.employee_id,e.name
-- order by employee_id 














select e.employee_id,e.name,count(m.reports_to) as reports_count,round(avg(m.age)) as average_age from Employees e 
join Employees m on e.employee_id = m.reports_to 
group by e.employee_id,e.name
order by e.employee_id