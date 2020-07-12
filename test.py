import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_table = "CREATE TABLE  users (id INTERGER PRIMARY KEY, username text, password text)"
"""
this is assigning the sql commands to create a table to a variable
called "create_table"
the table will have the following properties
    - name of table: users
    - field on the table:
        - id (intger)
        - username (text)
        - password (text)
"""

cursor.execute(create_table)
"""
this will execute the sql command to create a table, that command is
assigned to the variable "create_table"
"""

user = (1, 'glitch', 'cisco')
"""
this is a tupule that has the record entries for a user record
it is assign to a variable and will be used with a sql command to
insert the values into the "users" table
"""


insert_query = "INSERT INTO users VALUES (?, ?, ?)"
"""
this is assigning the sql commands to insert the values into the
"users" table to create a record for a user
"""

cursor.execute(insert_query, user)
"""
the "cursor.execute" method will take the sql commands assigned to
the variable "insert_query" to insert data into the "users" table and
take the values from the variable "user" as values for the record
"""


users = [
    (2, 'glitch2', 'cisco2'),
    (3, 'glitch3', 'cisco3')
]
"""
this a list that contains 2 user along with their properties
this will be used by the "cursor,executemany()" to enter many user
records into the "user" table
"""

cursor.executemany(insert_query, users)
"""
to enter many user records into the "user" table
"""

select_query = "SELECT * FROM users"
"""
this is assigning the sql command to retreive data from the "users"
table
the "*" will take data from every field (column) in the table
if you want to get date from a specific column, replace "*" with the
name of the column (e.g. "id","username","password")
"""

for row in cursor.execute(select_query):
    print(row)
"""
after "cursor.execute" executes the sql command it will be saved as a
list in memory
each row of data will have its own index just like a normal list
the "for" loop will interate over the in memory list and print a row
of data on a new line
"""



connection.commit()
connection.close()






