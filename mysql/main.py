

# pip install mysql-connector-python

# https://www.w3schools.com/python/python_mysql_create_db.asp


# empleados  (nombre, apellido, Rut, dirección)
# clientes   (nombre, apellido, Rut, dirección)

import mysql.connector

_db = "restaurant"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=_db
)

print(mydb)

mycursor = mydb.cursor()



# crear base de datos
# mycursor.execute("CREATE DATABASE "+_db)

# crear tablas
def createTables():
    mycursor.execute("""
                        CREATE TABLE clientes (
                            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(50),
                            apellido VARCHAR(50),
                            rut VARCHAR(50),
                            direccion VARCHAR(50)
                        )
                    """
    )

    mycursor.execute("""
                        CREATE TABLE empleados (
                            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(50),
                            apellido VARCHAR(50),
                            rut VARCHAR(50),
                            direccion VARCHAR(50)
                        )
                    """
    )

# createTables()

def insertData():
    # crear empleado
    sql = "INSERT INTO empleados (nombre, apellido, rut, direccion) VALUES (%s, %s, %s, %s)"
    val = ("Francisco", "Verdugo", "18345296-7", "Lira 443")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    # crear cliente
    sql = "INSERT INTO clientes (nombre, apellido, rut, direccion) VALUES (%s, %s, %s, %s)"
    val = ("Ayleen", "Bertini", "17345296-7", "Alvares 455")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


# insertData()

# leer clientes
# <class 'tuple'>
# (1, 'Francisco', 'Verdugo', '18345296-7', 'Lira 443')

def readTables():
    mycursor.execute("SELECT * FROM clientes")
    myresult = mycursor.fetchall()
    for x in myresult:
      # print(type(x))
      print(x)

    # leer empleados
    mycursor.execute("SELECT * FROM empleados")
    myresult = mycursor.fetchall()
    for x in myresult:
      # print(type(x))
      print(x)


readTables()



# eliminar clientes






# end
