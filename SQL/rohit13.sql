select * from emp;
select * from dept;
--selecting data from both tables by specifying join condition
select * from emp e,dept d where d.deptno=e.deptno;
select e.sal,e.ename,d.dname from emp e,dept d; // where d.deptno=e.deptno;
-- selecting the data from both table by specifying  join condition with filter condition 
select e.sal,e.job,e.mgr,d.dname from emp e,dept d where e.deptno= d.deptno and d.dname='ACCOUNTING';
select e.ename ,e.sal,e.job,e.mgr,d.dname from emp e join dept d on e.deptno = d.deptno where d.dname='ACCOUNTING'; 