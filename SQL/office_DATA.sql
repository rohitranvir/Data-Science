SELECT * FROM ASHOKIT_DEPT;
SELECT * FROM ASHOKIT_PROJECTS;
SELECT * FROM ASHOKIT_MANAGERS;
SELECT * FROM ASHOKIT_EMP;

select ae.emp_name,ad.dept_name from ashokit_emp ae join ashokit_dept ad on ae.dept_id =ad.dept_id;

-- Display employee name and departname ,emp name,manager name  belonging too

SELECT * FROM ASHOKIT_EMP;  //----ename
SELECT * FROM ASHOKIT_DEPT; //---department name
SELECT * FROM ASHOKIT_MANAGERS; //--manager name
-- Common column bet emp and dept  is dept_id
--Common coluumn bet dept and managers is dept_id
--Common coluumn bet emp and managers is manager_id and dept_id

--Writing Sql Query
select emp_id,emp_name,dept_name,manager_name 
from ashokit_emp ae join ashokit_dept ad on ae.dept_id = ad.dept_id 
join ashokit_managers am ON am.manager_id=ae.manager_id
order by emp_id ASC; 

select ae.emp_id,ae.emp_name,ad.dept_name from ashokit_emp ae left join ashokit_dept ad on ae.dept_id=ad.dept_id order by ae.emp_id asc;
