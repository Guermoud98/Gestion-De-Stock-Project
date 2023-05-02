from connexion import connexion
from utilisateur import utilisateur


class utilisateurDAO:

    def ajouterUser(self, user):
        try:
            # If you are using the connexion class to create a connection object, then you should use the conn attribute of the connection object to create the cursor instead of using the cursor() method
            cnx = connexion()
            cursor = cnx.conn.cursor()
            query = "INSERT INTO utilisateur(nom, password) VALUES (%s, %s)"
            values = (user.nom, user.password)
            cursor.execute(query, values)
            cnx.conn.commit()
            cursor.close()
            cnx.conn.close()
        except Exception as e:
            print(f"An error occurred: {e}")

    def afficherUsers(self):
        try:
            cnx = connexion()
            self.cursor = cnx.conn.cursor()
            query = "SELECT * FROM utilisateur"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Exception as e:
            print(f"An error occurred: {e}")
        


user = utilisateur("ss", "han22")
u = utilisateurDAO()
u.ajouterUser(user)
u.afficherUsers()