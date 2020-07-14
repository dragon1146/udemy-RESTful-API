import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)


# item = ('test', '12.89')
# insert_query = 
cursor.execute("INSERT INTO items VALUES ('test', 10.99)")


connection.commit()
connection.close()






