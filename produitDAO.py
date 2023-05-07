from produit import produit
from connexion import connexion
from admin import admin


class produitDAO:
    def __init__(self):
        self.cnx = connexion()
        self.cursor = self.cnx.conn.cursor()

    def ajouterProduit(self, produit, user):
        try:
            query = "INSERT INTO produit(nom, prix, qte_stock, seuil_alerte, date_derniere_entree, date_derniere_sortie,image_produit,id_admin)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            with open(produit.image_produit, 'rb') as file:
                image_data = file.read()
            values = (produit.nom, produit.prix, produit.qte_stock, produit.seuil_alerte,
                      produit.date_premiere_entree, produit.date_derniere_sortie, image_data, user.id_admin)
            self.cursor.execute(query, values)
            self.cnx.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def afficherProduits(self):
        try:
            query = "SELECT * FROM produit"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def rechercherProduit(self, nom, prix, qte_stock, date_derniere_sortie):
        try:
            query ="SELECT * FROM produit WHERE (nom=%s AND prix=%s AND qte_stock=%s AND date_derniere_sortie=%s) "
            values=(nom, prix, qte_stock, date_derniere_sortie)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Exception as e:
            print(f"An error occurred: {e}")

#p=produitDAO()
#p.rechercherProduit("mimi",12.9,12,13)