-- with date_cte as (
--     select player_id, min(event_date) as first_login_date from Activity group by player_id
-- )

-- select round(sum(datediff(a.event_date,t.first_login_date) = 1) / count(distinct a.player_id),2) as fraction from
-- Activity a join date_cte t on a.player_id = t.player_id


















with date_cte as(
select player_id,min(event_date) as first_login from Activity group by player_id
)

select round(sum(datediff(a.event_date,t.first_login) = 1) / count(distinct a.player_id),2) as  fraction 
from Activity a
join date_cte t on a.player_id = t.player_id