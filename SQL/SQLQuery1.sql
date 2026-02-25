select * from EMP;
alter table emp add  gender char(20);
alter table emp drop column mgr,comm;
EXEC sp_help 'EMP';
ALTER TABLE EMP
DROP CONSTRAINT PK__EMP__14CCF2EE85728319;
-- => modify column sal datatype to smallINT ?
ALTER TABLE EMP
ALTER COLUMN EMPNO SMALLINT;

ALTER TABLE EMP
ALTER COLUMN ENAME VARCHAR(6);

-- Drop Commmand
F