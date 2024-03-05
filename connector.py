import mysql.connector

mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM ")

# Obtener los resultados
for row in mycursor.fetchall():
    print(row)

mydb.close()
