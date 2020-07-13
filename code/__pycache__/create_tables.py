import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_table)


user = (1, 'glitch', 'cisco')


insert_query = "INSERT INTO users VALUES (?, ?, ?)"


cursor.execute(insert_query, user)



users = [
    (2, 'glitch2', 'cisco2'),
    (3, 'glitch3', 'cisco3')
]


cursor.executemany(insert_query, users)


select_query = "SELECT * FROM users"


for row in cursor.execute(select_query):
    print(row)




connection.commit()
connection.close()






