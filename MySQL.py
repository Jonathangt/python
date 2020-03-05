import pymysql
#pip install PyMySQLgit 
class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', #ip si es remota
            user='root',
            password='',
            db='python'
        )

        self.cursor = self.connection.cursor()
        #print("Se conecto!!")

    def select_user(self, id):
        sql = 'SELECT * FROM users WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()#para obtener un registro
            #print("id", user[0])
            #print("Username", user[1])
            #print("email", user[2])
            print(user)

        except Exception as e:
            raise

    def select_users_all(self):
        sql = 'SELECT * FROM users'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for users in users:
            #  print("id", user[0])
            #  print("Username", user[1])
            #  print("email", user[2])
            #   print("_______\n")
             print(users)
        except Exception as ee:
            raise
    
    def update_user(self, id, username):
        sql= "UPDATE users SET user='{}' WHERE id ={}".format(username, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        
        except Exception as e:
            raise

    def close(self):
        self.connection.close

database = DataBase()
#enviamos el id del user a actualizar
database.select_user(2)
#cambiamos los datos
database.update_user(2, 'Maria Belen')
#consultamos los cambios
#self.select_user(2)
database.select_users_all()

database.close