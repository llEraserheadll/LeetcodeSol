-- # Write your MySQL query statement below
-- # SELECT SUM(tiv_2016)
-- # FROM Insurance;

-- -- tiv
-- WITH tiv_count AS(
--     SELECT tiv_2015, COUNT(tiv_2015)
--     FROM Insurance
--     GROUP BY tiv_2015
--     HAVING COUNT(tiv_2015) > 1
-- ),
-- location_unique AS(
--     SELECT CONCAT(lat, ',', lon) AS lat_lon_pair
--     FROM Insurance
--     GROUP BY lat_lon_pair
--     HAVING COUNT(lat_lon_pair) = 1
-- )

-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM Insurance 
-- WHERE (tiv_2015 IN (SELECT tiv_2015 FROM tiv_count)) AND (CONCAT(lat, ',', lon) IN (SELECT lat_lon_pair FROM location_unique));
















with count_cte as(
select tiv_2015,count(tiv_2015) from Insurance group by tiv_2015 having count(tiv_2015) > 1
),
unique_location as (
    select concat(lat,',',lon) as unique_loc from Insurance group by unique_loc having count(unique_loc) = 1
)

select round(sum(tiv_2016),2) as tiv_2016 from Insurance where tiv_2015 in(select tiv_2015 from count_cte) and 
concat(lat,',',lon) in (select unique_loc from unique_location)