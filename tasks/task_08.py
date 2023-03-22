import pymysql.cursors
from mysql_queries.queries import queries_collection


connection = pymysql.connect(host="localhost", user="root", password="verde",
                            database="pymysql_tutorial", charset='utf8mb4')


def execute_queries(mysql_queries):
    try:
        cursor = connection.cursor()
    except Exception as e:
        print(f'Exception: {e} as ocurred when getting a cursor')

    all_emps_str = "SELECT * FROM EMPLOYEES"

    for key, value in mysql_queries.items():
        if key == "select_e_names":
            try:
                before_del = cursor.execute(all_emps_str)
                print(f'Employees before deletion: {before_del}')
            except Exception as beforedel:
                print(f'Exception: {beforedel} as occured when trying to select '
                       'all employees before deleting')

        try:
            cursor.execute(value)
        except Exception as sqle:
            print(f'Exception: {sqle} as occured when performing query: {value}')

    try:
        after_del = cursor.execute(all_emps_str)
        print(f'Employees after deletion: {after_del}')
    except Exception as afterdel:
                print(f'Exception: {afterdel} as occured when trying to select '
                       'all employees before deleting')
    finally:
        connection.close()

execute_queries(queries_collection)








