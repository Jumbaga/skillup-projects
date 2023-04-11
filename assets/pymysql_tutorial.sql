USE pymysql_tutorial;
SET SESSION sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
DROP TABLE IF EXISTS EMPLOYEES, TEAMS, MANAGERS, MANAGER_REGISTRATIONS;
DROP VIEW IF EXISTS TEAM_NAMES_AND_NUMBER_OF_EMPLOYEES, EMPLOYEES_SALARIES, MIN_MAX_EMP_SALARIES;

CREATE TABLE TEAMS(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(50),
    location VARCHAR(50) DEFAULT 'Lisabon',
    CHECK(location IN ('Lisabon', 'Porto', 'Coimbra', 'Aveiro'))
);

CREATE TABLE EMPLOYEES (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    tm_id INT,
    name VARCHAR(40)NOT NULL,
    phone VARCHAR(12)NOT NULL,
    date_hired DATE NOT NULL,
    salary DECIMAL(7,2) NOT NULL,
    FOREIGN KEY (tm_id) REFERENCES TEAMS(id)
);

INSERT INTO TEAMS(name, location)
VALUES ('Marketing', 'Porto'), 
	   ('Developers', 'Lisabon'),
       ('HR', 'Coimbra');
      
CREATE TABLE MANAGERS(
	emp_id INT UNIQUE,
    tm_id INT UNIQUE,
    start_date DATE,
    end_date DATE NULL,
    PRIMARY KEY (emp_id, tm_id, start_date),
    FOREIGN KEY (tm_id) REFERENCES TEAMS(id),
    FOREIGN KEY (emp_id) REFERENCES EMPLOYEES(id) ON DELETE CASCADE,
	CHECK (end_date >= start_date)
 );

CREATE TABLE MANAGER_REGISTRATIONS(
	emp_id INT,
	tm_id INT,
	start_date DATE
);

INSERT INTO EMPLOYEES (tm_id, name, phone, date_hired, salary)
VALUES (1, 'Ludacris', '919191910', '2021-01-01', 1000.50), 
	   (2, 'Vitor', '191919190', '2022-06-01', 1250.75),
       (3, 'John Doe', '212121212', '2015-04-25', 1700.20),
       (3, 'John Doe', '939393939', '2018-01-18', 1800.01),
       (1, 'Madmen', '111111111', '2018-01-18', 2000.5),
       (2, 'Milan', '222222222', '2018-01-18', 2200.75),
       (3, 'Ellon Cusk', '333333333', '2018-01-18', 3000.99);
      
INSERT INTO MANAGER_REGISTRATIONS(emp_id, tm_id, start_date)
SELECT e.id, e.tm_id, curdate(                                   ) start_date FROM EMPLOYEES e WHERE e.salary >=2000;

INSERT INTO MANAGERS(emp_id, tm_id, start_date)
SELECT mr.emp_id, mr.tm_id, mr.start_date FROM MANAGER_REGISTRATIONS mr;

CREATE VIEW TEAM_NAMES_AND_NUMBER_OF_EMPLOYEES
AS SELECT
	t.name AS name,
	COUNT(*) AS employee_count
	FROM 	
		TEAMS t
		INNER JOIN EMPLOYEES e 
		ON t.id = e.tm_id
	GROUP BY t.name;

CREATE VIEW EMPLOYEES_SALARIES
AS SELECT	
	e.name AS name,
	SUM(e.salary) AS sum_salaries,
	AVG(e.salary) AS avg_salaries
FROM EMPLOYEES e 
GROUP BY e.name;

CREATE VIEW MIN_MAX_EMP_SALARIES
AS SELECT
	MIN(salary),
	MAX(salary)
FROM EMPLOYEES;






