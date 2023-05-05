from connexion import connexion
from admin import admin


class adminDAO:
    def __init__(self):
        self.cnx = connexion()
        self.cursor = self.cnx.conn.cursor()

    def ajouterAdmin(self, user):
        try:
            query = "INSERT INTO admin(nom, password) VALUES (%s, %s)"
            values = (user.nom, user.password)
            self.cursor.execute(query, values)
            self.cnx.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def afficherAdmins(self):
        try:
            query = "SELECT * FROM admin"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Exception as e:
            print(f"An error occurred: {e}")

    def afficherSpecificAdmin(self, username, password):
        try:
            query = "SELECT * FROM admin WHERE nom= %s AND password=%s"
            values = (username, password)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            if len(result) > 0:
             return True
            else:
              return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  

    def modifierAdmin(self,id, password):
        try:
            query = "UPDATE  admin SET password = %s WHERE id = %s"
            values = (password, id)
            self.cursor.execute(query, values)
            self.cnx.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def supprimerAdmin(self,id):
        try:
            query = "DELETE FROM admin WHERE id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            self.cnx.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
#ajouter
admin = admin("qqlx", "gqg")
a = adminDAO()
a.ajouterAdmin(admin)
#a.afficherAdmins()
#modifier
#a.modifierAdmin(2,"lol")
#a.afficherAdmins()
#supprimer admin
#a = adminDAO()
#a.afficherAdmins()
if(a.afficherSpecificAdmin("d",12233) == True):
    print("existe")
else:
    print("doesnt")