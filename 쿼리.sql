CREATE DATABASE python

CREATE TABLE emp(
	e_id VARCHARACTER(20),
	e_name VARCHARACTER(100),
	sex VARCHARACTER(1),
	addr VARCHARACTER(400));
	
INSERT INTO emp(e_id,e_name,sex,addr) VALUES('1','1','1','1');
INSERT INTO emp(e_id,e_name,sex,addr) VALUES('2','2','2','2');
INSERT INTO emp(e_id,e_name,sex,addr) VALUES('3','3','3','3');

UPDATE emp SET e_name='6',sex='6',addr='6' WHERE e_id='3';

DELETE FROM emp WHERE e_id='5';

SELECT * FROM emp WHERE e_id='1';empmem