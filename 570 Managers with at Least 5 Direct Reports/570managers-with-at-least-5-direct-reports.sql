-- # Write your MySQL query statement below
-- Select m.name
-- from employee as e
-- inner join employee as m
-- on e.managerId=m.id
-- group by e.managerId
-- HAVING COUNT(m.id) >= 5;





select e.name from Employee e join Employee m on e.id = m.managerId group by m.managerId having count(m.managerId) >= 5








