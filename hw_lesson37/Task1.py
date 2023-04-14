import psycopg2

"""
Task 1

Joins

Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)

1.write a query in SQL to display the first name, last name, department number, and department name for each employee
2.write a query in SQL to display the first and last name, department, city, and state province for each employee
3.write a query in SQL to display the first name, last name, department number, and department name,
for all employees for departments 80 or 40
4.write a query in SQL to display all departments including those where does not have any employee
5.write a query in SQL to display the first name of all employees including the first name of their manager
6.write a query in SQL to display the job title, full name (first and last name ) of the employee,
and the difference between the maximum salary for the job and the salary of the employee
7.write a query in SQL to display the job title and the average salary of employees
7.write a query in SQL to display the full name (first and last name),
and salary of those employees who work in any department located in London
9.write a query in SQL to display the department name and the number of employees in each department

table employees:
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


# write a query in SQL to display the first name, last name, department number, and department name for each employee
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT t1.c2 as first_name, t1.c3 as last_name, t1.c11 as department_number, t2.c2 as department_name
            FROM employees as t1 LEFT JOIN department as t2 on t1.c11 = t2.c1;
            """
        )

# write a query in SQL to display the first and last name, department, city, and state province for each employee
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT t1.c2 as first_name, t1.c3 as last_name, t1.c11 as department_number, t2.c2 as department_name,
            t3.c4 as city, t3.c5 as state_province
            FROM employees as t1 LEFT JOIN department as t2 on t1.c11 = t2.c1
            LEFT JOIN locations as t3 on t2.c4 = t3.c1;
            """
        )

# write a query in SQL to display the first name, last name, department number, and department name,
# for all employees for departments 80 or 40
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT t1.c2 as first_name, t1.c3 as last_name, t1.c11 as department_number, t2.c2 as department_name
            FROM employees as t1 LEFT JOIN department as t2 on t1.c11 = t2.c1
            WHERE (c11 = 80 or c11 = 40);
            """
        )

# write a query in SQL to display all departments including those where does not have any employee
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT t1.c2 as first_name, t1.c3 as last_name, t1.c11 as department_number, t2.c2 as department_name
            FROM employees as t1 RIGHT JOIN department as t2 on t1.c11 = t2.c1;
            """
        )

# write a query in SQL to display the first name of all employees including the first name of their manager
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT t1.c2 as first_name, t1.c3 as last_name, t2.c2 as first_name_manager, t2.c3 as last_name_manager
            FROM employees as t1 INNER JOIN employees as t2 on t1.c10 = t2.c1;
            """
        )

# write a query in SQL to display the job title, full name (first and last name ) of the employee,
# and the difference between the maximum salary for the job and the salary of the employee
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT t2.job_title, (t1.c2 || ' ' || t1.c3) as full_name, (t2.max_salary - t1.c8) as different
            FROM employees as t1 INNER JOIN jobs as t2 on t1.c7 = t2.job_id;
            """
        )

# write a query in SQL to display the job title and the average salary of employees
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT t2.job_title, (t2.max_salary + t2.min_salary + t1.c8) as avg_salary
            FROM employees as t1 INNER JOIN jobs as t2 on t1.c7 = t2.job_id;
            """
        )

# write a query in SQL to display the full name (first and last name),
# and salary of those employees who work in any department located in London
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT (t1.c2 || ' ' || t1.c3) as full_name, t1.c8 as salary
            FROM employees as t1 INNER JOIN department as t2 on t1.c11 = t2.c1
            WHERE t2.c4  in (SELECT c1 FROM locations WHERE c4 = 'London');
            """
        )

# write a query in SQL to display the department name and the number of employees in each department
    with connection.cursor() as cursors:
        cursors.execute(
            """
            SELECT t2.c2 as department_name, count(*) as  number_employees
            FROM employees as t1 INNER JOIN department as t2 on t1.c11 = t2.c1
            GROUP BY t2.c2
            ORDER BY t2.c2;
            """
        )

except Exception as e:
    print('Error', e)
finally:
    if connection:
        connection.close()
        print('Close')
