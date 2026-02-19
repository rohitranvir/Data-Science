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