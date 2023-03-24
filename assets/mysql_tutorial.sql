USE pymysql_tutorial;
DROP TABLE IF EXISTS EMPLOYEES, TEAMS;
CREATE TABLE EMPLOYEES (
    id INT PRIMARY KEY NOT NULL CHECK (0<=id<= 999),
    tm_id INT,
    name VARCHAR(40),
    phone VARCHAR(12),
    date_hired DATE
);
CREATE TABLE TEAMS(
	id int PRIMARY KEY NOT NULL CHECK(0<=id<=999),
    name VARCHAR(50),
    location VARCHAR(50) DEFAULT 'Lisabon' CHECK(location='Lisabon' OR location='Porto' OR location='Coimbra' OR location='Aveiro'),
    manager VARCHAR(50)
);
    
ALTER TABLE EMPLOYEES
ADD FOREIGN KEY (tm_id) REFERENCES TEAMS(id); 

INSERT INTO TEAMS(id, name, location, manager)
VALUES (1, 'Marketing', 'Porto', 'Madmen'), 
	   (2, 'Developers', 'Lisabon', 'Milan'),
       (3, 'Supervisors', 'Coimbra', 'Ellon Cusk');

INSERT INTO EMPLOYEES (id, tm_id, name, phone, date_hired)
VALUES (1, 1, 'Ludacris', '919191910', '2021-01-01'), 
	   (2, 2, 'Vitor', '191919190', '2022-06-01'),
       (3, 3, 'John Doe', '212121212', '2015-04-25'),
       (4, 3, 'John Doe', '939393939', '2018-01-18');

SELECT name FROM EMPLOYEES;

SELECT e.phone FROM EMPLOYEES AS e, TEAMS AS t
WHERE t.id = e.tm_id AND t.location = 'Porto';

SELECT e.name, MIN(e.date_hired)
FROM EMPLOYEES as e
INNER JOIN TEAMS as t ON t.id=e.tm_id
AND e.name = 'John Doe' AND t.name = 'Supervisors';

DELETE e
FROM EMPLOYEES e INNER JOIN TEAMS t
ON t.id = e.tm_id 
WHERE
    t.name = 'Marketing';

SELECT * FROM EMPLOYEES;