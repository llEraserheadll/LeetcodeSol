-- # Write your MySQL query statement below
-- with cte1 as(
-- select visited_on, sum(amount) as amount from customer group by visited_on
-- )
-- ,cte as(
-- select visited_on,sum(amount) over(rows between 6 preceding and current row) as amount, avg(amount) over(rows between 6 preceding and current row) as average_amount from cte1 group by visited_on order by visited_on
-- )

-- select visited_on,round(amount,2) as amount,round(average_amount,2) as  average_amount from cte where visited_on >=(select date_add(min(visited_on),interval 6 day) from customer)














with sales as(
    select visited_on, sum(amount) as amount from Customer group by visited_on
),
sum_sales as(
    select visited_on,sum(amount) over(rows between 6 preceding and current row) as amount,
    avg(amount) over(rows between 6 preceding and current row) as avg_amount from sales group by visited_on
    order by visited_on
)

select visited_on,round(amount,2) as amount,round(avg_amount,2) as average_amount from sum_sales where 
visited_on >= (select min(visited_on) + interval 6 day from sum_sales) order by visited_on














