use campusx;
-- select * from(
-- select user_id,monthname(date) as 'month',sum(amount)as 'total',
-- rank() over(partition by monthname(date) order by sum(amount) desc ) as 'month_rank'
-- from orders group by user_id,monthname(date) order by monthname(date))t
-- where t.month_rank<3

select * from (select student_id , name,branch,marks,
dense_rank() over(partition by branch  order by marks) as 'rank'
from marks)t
where t.rank;

select student_id , name,branch,marks,
last_value(marks) over(partition by branch order by marks desc) as 'first_value'
from marks;


select student_id , name,branch,marks,
last_value(name) over(partition by branch order by marks desc
					rows between unbounded preceding and unbounded following) as 'first_value'
from marks;

select student_id , name,branch,marks,
nth_value(marks,2) over(partition by branch order by marks desc
					rows between unbounded preceding and unbounded following) as 'first_value'
from marks;


select t1.name,t1.branch,t1.marks from (select *,
first_value(name) over(partition by branch order by marks desc) as "topper_name",
first_value(marks) over(partition by branch order by marks desc) as "topper_marks"
from marks)t1
where t1.name=topper_name and t1.marks=topper_marks	