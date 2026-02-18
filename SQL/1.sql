use campusx;
select * from marks;
-- select branch,sum(marks)
-- from marks 
-- group by branch
select * ,
avg(marks) over(partition by branch) as marks
from marks;

--  Find all the students who have marks higher than the avg marks of their respective
-- branch
select * from (select * ,avg(marks) 
over(partition by branch)as 'mrk_marks' from marks)t
where t.marks>t.mrk_marks;

select *,
rank() over(partition by branch order by marks desc),
dense_rank() over(partition by branch order by marks desc)
from marks;

 
