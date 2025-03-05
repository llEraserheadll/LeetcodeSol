-- with sales_cte as(
--     select product_id,min(year) as first from Sales group by product_id
-- )

-- select s.product_id,s.year as first_year,s.quantity,s.price from Sales s
-- join sales_cte c on s.product_id = c.product_id and s.year = c.first 







with sale_cte as(
    select product_id,min(year) as first_year from Sales group by product_id
)

select s.product_id,p.first_year,s.quantity,s.price from Sales s join sale_cte p on s.product_id = p.product_id
 and s.year = p.first_year


