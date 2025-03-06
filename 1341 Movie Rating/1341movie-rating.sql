-- # Write your MySQL query statement below
-- (select m.title as results from MovieRating r join Movies m on r.movie_id = m.movie_id where r.created_at between  '2020-02-01' and '2020-02-28' group by m.title order by avg(r.rating) desc,m.title asc limit 1)
-- union all
-- (select u.name as results from Movierating r join Users u on r.user_id = u.user_id  group by u.name order by count(r.user_id) desc,u.name asc limit 1)








(select u.name as results from MovieRating a join Users u on a.user_id = u.user_id group by a.user_id
 order by count(a.rating) desc,u.name limit 1)
union all
(select s.title as results from MovieRating m join Movies s on s.movie_id = m.movie_id 
where m.created_at between '2020-02-01' and '2020-02-28' 
 group by m.movie_id order by avg(m.rating) desc,s.title limit 1)










