import mysql.connector

class connexion:
   def __init__(self):
       try:
           self.conn = mysql.connector.connect(
               host = "localhost",
               user = "root",
               database = "stock",
               password = "maria1998"
           )
           print("la connexion avec la base de donnée est réussie")
   
       except mysql.connector.Error as error:
            print(f"Erreur lors de la connexion à la base de données: {error}")
   
   
   
   
#cnx = connexion(host="localhost", user="root", database="stock", password="maria1998")
  