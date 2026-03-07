select DEPTNO,count(*) 
from emp 
group by DEPTNO 
having count(*)>3;