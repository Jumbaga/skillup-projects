queries_collection = {}

drop_existing_tables = "DROP TABLE IF EXISTS EMPLOYEES, TEAMS;"
queries_collection["drop"] = drop_existing_tables
create_employees = "CREATE TABLE EMPLOYEES( id INT PRIMARY KEY NOT NULL CHECK (0<=id<= 999), tm_id INT,name VARCHAR(40), phone VARCHAR(12), date_hired DATE);"
queries_collection["create_emps"] = create_employees
create_teams = "CREATE TABLE TEAMS( id int PRIMARY KEY NOT NULL CHECK(0<=id<=999), name VARCHAR(50), location VARCHAR(50) DEFAULT 'Lisabon' CHECK(location='Lisabon' OR location='Porto' OR location='Coimbra' OR location='Aveiro'), manager VARCHAR(50));"
queries_collection["create_teams"] = create_teams
add_foreign_key = "ALTER TABLE EMPLOYEES ADD FOREIGN KEY (tm_id) REFERENCES TEAMS(id);"
queries_collection["foreign_key"] = add_foreign_key
insert_teams = "INSERT INTO TEAMS(id, name, location, manager) VALUES (1, 'Marketing', 'Porto', 'Madmen'), (2, 'Developers', 'Lisabon', 'Milan'), (3, 'Supervisors', 'Coimbra', 'Ellon Cusk');"
queries_collection["insert_teams"] = insert_teams
insert_employees = "INSERT INTO EMPLOYEES (id, tm_id, name, phone, date_hired) VALUES (1, 1, 'Ludacris', '919191910', '2021-01-01'), (2, 2, 'Vitor', '191919190', '2022-06-01'), (3, 3, 'John Doe', '212121212', '2015-04-25'), (4, 3, 'John Doe', '939393939', '2018-01-18');"
queries_collection["insert_employees"] = insert_employees
employee_names_query = "SELECT name FROM EMPLOYEES;"
queries_collection["select_e_names"] = employee_names_query
porto_phones_query = "SELECT e.phone FROM EMPLOYEES AS e, TEAMS AS t WHERE t.id = e.tm_id AND t.location = 'Porto';"
queries_collection["porto_phones"] = porto_phones_query
oldest_supervisor_query = "SELECT e.name, MIN(e.date_hired) FROM EMPLOYEES as e INNER JOIN TEAMS as t ON t.id=e.tm_id AND e.name = 'John Doe' AND t.name = 'Supervisors';"
queries_collection["oldest_supervisor"] = oldest_supervisor_query
delete_marketing_employees_query = "DELETE e FROM EMPLOYEES e INNER JOIN TEAMS t ON t.id = e.tm_id WHERE t.name = 'Marketing';"
queries_collection["delete_marketing_emps"] = delete_marketing_employees_query

