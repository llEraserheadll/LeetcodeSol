-- # Write your MySQL query statement below
-- select s.student_id , s.student_name , sub.subject_name,count(e.student_id) as attended_exams from Students s cross join Subjects sub left join Examinations e on s.student_id =  e.student_id and sub.subject_name = e.subject_name
-- group by s.student_id,s.student_name, sub.subject_name 
-- order by s.student_id,sub.subject_name













select s.student_id,s.student_name,j.subject_name,count(e.student_id) as attended_exams from Students s cross join Subjects j
left join Examinations e on e.student_id = s.student_id and e.subject_name = j.subject_name
group by s.student_id,s.student_name,j.subject_name
order by s.student_id,s.student_name








