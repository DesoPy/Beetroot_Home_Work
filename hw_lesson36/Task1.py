import psycopg2

"""
Task 1

Create a table

Create a table of your choice inside the sample SQLite database, rename it, and add a new column.
Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.

As a solution to this task, create a file named: task1.sql,
with all the SQL statements you have used to accomplish this task
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

# Create a table of your choice
    with connection.cursor() as cursors:
        cursors.execute(
            """
            CREATE TABLE first23(
            id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL,
            second_name varchar(50) NOT NULL,
            full_name varchar(50) NOT NULL
            );
            """
        )

# rename it
    with connection.cursor() as cursors:
        cursors.execute(
            """
            ALTER TABLE IF EXISTS first23
            RENAME TO new_first;
            """
        )

# add a new column
    with connection.cursor() as cursors:
        cursors.execute(
            """
            ALTER TABLE IF EXISTS new_first ADD COLUMN birthday date;
            """
        )

# Insert a couple rows inside your table
    with connection.cursor() as cursors:
        cursors.execute(
            """
            INSERT INTO new_first (id, first_name, second_name, full_name, birthday)
                        VALUES (1, 'Test15', 'Test25', 'Test1_Test555','1991-02-03');
            INSERT INTO new_first (id, first_name, second_name, full_name, birthday)
                        VALUES (2, 'Test5', 'Test5', 'Test1_Test555','1996-05-04');
            INSERT INTO new_first (id, first_name, second_name, full_name, birthday)
                        VALUES (3, 'Test188', 'Test88', 'Test888_Test2','1997-08-09');
            """
        )

# Insert a couple rows inside your table
    with connection.cursor() as cursors:
        cursors.execute(
            """
            UPDATE new_first SET first_name = 'Update_First_Name', second_name = 'Update_Second_Name' where id = 25;
            """
        )

# drope table
    with connection.cursor() as cursors:
        cursors.execute(
            """
            DROP TABLE new_first;
            """
        )

except Exception as e:
    print('Error', e)
finally:
    if connection:
        connection.close()
        print('Close')
