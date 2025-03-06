-- -- # Write your MySQL query statement below
-- -- WITH cte AS(
-- --     SELECT id, salary,
-- --     DENSE_RANK() OVER(ORDER BY salary DESC) AS rank_num
-- --     FROM Employee
-- -- )

-- -- SELECT CASE WHEN MAX(rank_num) = 1 THEN NULL 
-- --     ELSE salary 
-- --     END AS SecondHighestSalary
-- -- FROM cte
-- -- WHERE rank_num = 2;

-- -- # SELECT
-- -- #     IFNULL(
-- -- #       (SELECT DISTINCT Salary
-- -- #        FROM Employee
-- -- #        ORDER BY Salary DESC
-- -- #         LIMIT 1 OFFSET 1),
-- -- #     NULL) AS SecondHighestSalary





-- SELECT MAX(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee)




select ifnull(
    (select distinct salary from employee order by salary desc limit 1 offset 1
),null) as secondHighestSalary