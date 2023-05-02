class admin:
    id = 0
    # constructeur

    def __init__(self, nom, password):
        admin.id += 1
        self.id = admin.id
        self.nom = nom
        self.password = password
