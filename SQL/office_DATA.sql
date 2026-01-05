create table ashokit_dept(
    dept_id varchar(10) primary key,
    dept_name varchar(50) unique not null
);
SELECT * FROM ASHOKIT_DEPT;
create table ashokit_managers(
    manager_id varchar(10) primary key,
    manager_name varchar(50) not null,
    dept_ID varchar(10) ,
    constraint fk_deptID
    foreign key (dept_ID) REFERENCES ashokit_dept(dept_id)
);
SELECT * FROM ASHOKIT_MANAGERS;
insert into ashokit_managers values('&manager_id','&manager_name','&dept_id');
create table ashokit_emp(
    emp_id varchar(10) primary key,
    emp_name varchar(50) not null,
    salary number not null,
    dept_id varchar(10), 
    manager_id varchar(10),
    constraint fk_dptid
    foreign key (dept_id)
    references ashokit_dept(dept_id),
    CONSTRAINT fk_mgr
    foreign key (manager_id)
    references ashokit_managers(manager_id)
);


INSERT INTO ASHOKIT_EMP VALUES('&EMP_ID','&emp_name',&salary,'&dept_id','&manager_id');
create table ashokit_projects(
    project_id varchar(10),
    project_name varchar(50),
    team_member_id varchar(50)
)
SELECT * from ashokit_projects;
insert into ashokit_projects values('&project_id','&project_name','&team_momber_id');