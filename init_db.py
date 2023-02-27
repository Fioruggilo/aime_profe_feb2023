import sqlite3

# Create the database
con = sqlite3.connect('./instance/aime_profe.db')

# Create a cursor to execute queries
cur = con.cursor() 

# delete the table if it exists
cur.execute('DROP TABLE IF EXISTS asistencias;')
#create the table
# id serial PRIMARY KEY means that the id will be autoincremented and will be the primary key
# VARCHAR(50) means VARIABLE CHARACTER and the field will be a string with a maximum of 50 characters
cur.execute("""CREATE TABLE asistencias (id serial PRIMARY KEY, 
apellido VARCHAR(50) NOT NULL, 
nombre VARCHAR(50) NOT NULL, 
ci VARCHAR(50) NOT NULL, 
asistencia INTEGER, 
grado VARCHAR(20) NOT NULL, 
justificativo VARCHAR(100) NOT NULL, 
fecha VARCHAR(20) NOT NULL)""")

#this is an example of how to insert data into the database
cur.execute('''INSERT INTO asistencias (id, apellido, nombre, ci, asistencia, grado, justificativo, fecha)
            VALUES(1, 'Parker', 'Peter', '1234567', 0, '3M', 'Tiene chimichurri', '27-02-2023'); 
            ''')

cur.execute('''INSERT INTO asistencias (id, apellido, nombre, ci, asistencia, grado, justificativo, fecha)
            VALUES(2, 'Wayne', 'Bruce', '1234568', 0, '3M', 'Ta ocupao', '27-02-2023'); 
            ''')

cur.execute('''INSERT INTO asistencias (id, apellido, nombre, ci, asistencia, grado, justificativo, fecha)
            VALUES(3, 'Kent', 'Clark', '1234569', 1, '3M', '', '27-02-2023'); 
            ''')

cur.execute('''INSERT INTO asistencias (id, apellido, nombre, ci, asistencia, grado, justificativo, fecha)
            VALUES(4, 'Eren', 'Jaegger', '1234560', 1, '3M', '', '27-02-2023'); 
            ''')

#commit the changes
con.commit()
#close the connection
cur.close()
con.close()