from asyncio.windows_events import NULL
from produit import produit
from connexion import connexion
from admin import admin
from login_interface import logged_in_admin


class produitDAO:
    def __init__(self):
        self.cnx = connexion()
        self.cursor = self.cnx.conn.cursor()
    def ajouterProduit(self, produit):
        try:
            query = "INSERT INTO produit(nom, prix, qte_stock, seuil_alerte, date_derniere_entree, date_derniere_sortie,nom_admin)  VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (produit.nom, produit.prix, produit.qte_stock, produit.seuil_alerte,
                      produit.date_premiere_entree, produit.date_derniere_sortie, logged_in_admin)
            self.cursor.execute(query, values)
            self.cnx.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            """ query = "INSERT INTO produit(nom, prix, qte_stock, seuil_alerte, date_derniere_entree, date_derniere_sortie,image_produit,id_admin)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            with open(produit.image_produit, 'rb') as file:
                image_data = file.read()
            values = (produit.nom, produit.prix, produit.qte_stock, produit.seuil_alerte,
                      produit.date_premiere_entree, produit.date_derniere_sortie, image_data, user.id_admin)
            self.cursor.execute(query, values)"""
              
    def afficherProduits(self):
        try:
            query = "SELECT * FROM produit"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
    # rechercher par nom
    def rechercherProduit(self, nom):
        try:
            query ="SELECT * FROM produit WHERE nom=%s  "
            values=(nom,)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return NULL
    def supprimerProduit(self, nom_produit):
        try:
            query = "DELETE FROM produit WHERE nom = %s"
            values = (nom_produit,)
            self.cursor.execute(query, values)
            self.connexion.commit()
            print("Product deleted successfully.")
            return True
                
           
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
#p=produitDAO()
#p.rechercherProduit("mimi",12.9,12,13)