import pymysql.cursors
#Importing queries dictionary
from mysql_queries.queries import queries_collection

#Getting connection object from pymysql.cursors module, passing dependencies for db connection
connection = pymysql.connect(host="localhost", user="root", password="verde",
                            database="pymysql_tutorial", charset='utf8mb4')

#Function that has a dictionary of mysql queries as a dependency and will try to execute all of them to query the db
def execute_queries(mysql_queries):
    try:
        #Getting cursor object from connection object to execute our queries and fecth our results
        cursor = connection.cursor()
    #Exception handling with a simple print    
    except Exception as e:
        print(f'Exception: {e} as ocurred when getting a cursor')

    #MySQL statement that selects all employees from the EMPLOYEES table
    all_emps_str = "SELECT * FROM EMPLOYEES"

    #Iterating through the queries 
    for key, value in mysql_queries.items():
        #There is a query on the provided dictionary that has "select_e_names" as a key and is executed
        #after the tables are populated, I want to check how many employees are there after populating.
        if key == "select_e_names":
            try:
                #Passing MySQL statement for the cursor to execute, selecting all employees
                before_del = cursor.execute(all_emps_str)
                #Printing  the number and all the rows of employees
                print(f'Employees before deletion: {before_del} \n {cursor.fetchall()}')
            #Exception handling with a simple print
            except Exception as beforedel_e:
                print(f'Exception: {beforedel_e} as occured when trying to select '
                       'all employees before deleting')
        #Trying to use cursor object to execute a query from the dictionary
        try:
            cursor.execute(value)
        #Exception handling with a simple print    
        except Exception as sql_e:
            print(f'Exception: {sql_e} as occured when performing query: {value}')

    try:
        #Last query on the dictionary was to delete all employees on the marketing department
        #so we are going to exectue the same query to all employees to check the number to print
        #and also printing all the EMPLOYEES table rows
        after_del = cursor.execute(all_emps_str)
        print(f'Employees after deletion: {after_del} \n {cursor.fetchall()}')
    #Exception handling with a simple print    
    except Exception as afterdel_e:
                print(f'Exception: {afterdel_e} as occured when trying to select '
                       'all employees after deleting')
    #Closing the db connection            
    finally:
        connection.close()

#Function call passing the queries imported
execute_queries(queries_collection)








