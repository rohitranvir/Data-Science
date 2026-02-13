Working With Sub Queries

Query-1: Display department details of employee smith?

SQL >> select * from dept where deptno IN(select deptno from emp where ename='SMITH');

Query-2: Display employee details who is working under SALES

SQL >> select * from emp where deptno=(select deptno from dept where dname='SALES');

Query-3: Display employee details whose salary is less than employee id as 7788 ?

SQL >> Select * from emp where sal <= (select sal from emp where empno=7788);

Query-4: Display employee details whose salary is less than 7788 and who are getting commission?

SQL >> select * from emp where sal <= (select sal from emp where empno=7788) and comm is not null;

Query-5: Display employee details who are working under Blake-Manager?

SQL >> select * from emp where mgr = (select empno from emp where upper(ename) ='BLAKE');

Query-6: Display employee details who are working in chicago ?

SQL >> select * from emp where deptno = (select deptno from dept where upper(location) ='CHICAGO');

Query-7: Display the employee details for second maximium salary.
SQL >> select * from emp where sal In (select max(sal) from emp where sal <(select max(sal) from emp));
