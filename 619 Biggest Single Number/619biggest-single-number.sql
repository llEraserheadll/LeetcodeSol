-- # Write your MySQL query statement belows
-- select max(num) as num from (select num from Mynumbers group by num having count(num)=1) as total












with count_cte as(
    select num from MyNumbers group by num having count(num) = 1
)

select max(num) as num from count_cte