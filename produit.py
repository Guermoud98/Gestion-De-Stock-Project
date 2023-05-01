class produit:
    id = 0
    # constructeur

    def __init__(self, nom, prix, qte_stock, seuil_alerte, date_premiere_entree, date_derniere_sortie, image_produit):
        produit.id += 1
        self.id = produit.id
        self.nom = nom
        self.prix = prix
        self.qte_stock = qte_stock
        self.seuil_alerte = seuil_alerte
        self.date_premiere_entree = date_premiere_entree
        self.date_derniere_sortie = date_derniere_sortie
        self.image_produit = image_produit
