import psycopg2

"""
#Select queries

Use the sample SQLite database hr.db
 - write a query to display the names (first_name, last_name) using alias name "First Name",
"Last Name" from the table of employees;
 - write a query to get the unique department ID from the employee table
 - write a query to get all employee details from the employee table ordered by first name, descending
 - write a query to get the names (first_name, last_name), salary,
PF of all the employees (PF is calculated as 12% of salary)
 - write a query to get the maximum and minimum salary from the employees table
 - write a query to get a monthly salary (round 2 decimal places) of each and every employee

c1 = employee_id
c2 = first_name
c3 = last_name
c4 = email
c5 = phone_number
c6 = hire_date
c7 = job_id
c8 = salary
c9 = commission_pct
c10 = manager_id
c11 = department_id
c12 = vg_Salary
"""

HOST = '3.71.99.74'
port = 5433
user = 'postgres'
password = 'RootBeet-101'
db_name = 'postgres'


try:
    connection = psycopg2.connect(
        host=HOST,
        port=port,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    with connection.cursor() as cursors:
        cursors.execute(
            'Select version();'
        )

        print(f'Selection version: {cursors.fetchone()}')


# write a query to display the names (first_name, last_name) using alias name "First Name",
# "Last Name" from the table of employees;
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT c2 as FirstName, c3 as LastName FROM employees;
            """
        )

# write a query to get the unique department ID from the employee table
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT DISTINCT (c11) as department_id FROM employees;
            """
        )

# write a query to get all employee details from the employee table ordered by first name, descending
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT * FROM employees ORDER BY c2 DESC;
            """
        )

# write a query to get the names (first_name, last_name), salary,
# PF of all the employees (PF is calculated as 12% of salary)
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT c2 as first_name, c3 as last_name, c8 as salary, c8 * 0.12 as PF  FROM employees;
            """
        )

# write a query to get the maximum and minimum salary from the employees table
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT MIN(c8) as min_salary, MAX(c8) as max_salary FROM employees;
            """
        )

# write a query to get a monthly salary (round 2 decimal places) of each and every employee
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT round(c8, 2) FROM employees;
            """
        )

except Exception as e:
    print('Error', e)
finally:
    if connection:
        connection.close()
        print('Close')
