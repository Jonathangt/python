"""
    pip install pyodbc
"""

import pyodbc 

conn = pyodbc.connect(
    "DRIVER={SQL Server Native Client 11.0};"
    "SERVER=JONATHAN\SQLEXPRESS;"
    "DATABASE=dummy;"
    "Trusted_Connection=yes;"
    "UID = Jonathan\Jonathan_;" 
    "PWD = amarillo;" 
)
print("Coneccion a dataBase ok")

def read(conn):
    print("--funcion read--")
    cursor = conn.cursor()
    cursor.execute("select * from dummy")
    for row in cursor:
        print(row)

def create(conn):
    print("\n--create--")
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO dummy(numero, nombreApellido) values(?,?);',
        (12345, 'prueba')
             
    )
    conn.commit()
    read(conn)

def update(conn):
    print("\n--update--")
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE dummy SET nombreApellido = ? WHERE numero=?;',
        ('newPrueba22', 12345)
    )
    conn.commit()
    read(conn)


def delete(conn):
    print("\n--delete--")
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM dummy WHERE numero =?;',
        (12345)
    )
    conn.commit()
    read(conn)
        

read(conn)
create(conn)
update(conn)
#delete(conn)
conn.close()