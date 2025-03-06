-- # Write your MySQL query statement below

-- select row_number() over() as id,student from Seat
-- order by if(mod(id,2) = 0,id-1,id+1)









select case 
when id % 2 = 1 and id + 1 <= (select max(id) from Seat) then id + 1
when id % 2 = 0 then id - 1
else id
end as id ,
student from Seat order by id








