import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
 
cursor.execute("DROP TABLE IF EXISTS students;")
cursor.execute(""" 
CREATE TABLE students (
	id INTEGER PRIMARY KEY  NOT NULL,
	name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL,
    grade VARCHAR(255),
    subjects VARCHAR(255)
               
);
""")
 
print("Table People is Ready!")
 