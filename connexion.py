import mysql.connector

class connexion:
   def __init__(self, host, user, database, password):
       try:
           self.conn = mysql.connector.connect(
               host = host,
               user = user,
               database = database,
               password = password
           )
           print("la connexion avec la base de donnée est réussie")
   
       except mysql.connector.Error as error:
            print(f"Erreur lors de la connexion à la base de données: {error}")
   
   
   
   
   
  