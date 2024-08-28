# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.customer_id)  as count_no_trans from Visits v
left join Transactions t on v.visit_id = t.visit_id
where transaction_id is NULL
group by customer_id
