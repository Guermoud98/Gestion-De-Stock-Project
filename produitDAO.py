from produit import produit
from connexion import connexion


class produitDAO:
    def __init__(self):
        self.cnx = connexion()
        self.cursor = self.cnx.conn.cursor()

    def ajouterProduit(self, produit, user):
        try:
            query = "INSERT INTO produit(nom,prix,qte_stock,seuil_alerte,date_derniere_entree,date_derniere_sortie,image_produit,id_admin)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
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

    