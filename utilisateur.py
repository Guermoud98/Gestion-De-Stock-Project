class utilisateur:
    id = 0
    #constructeur
    
    def __init__(self,nom,password):
        utilisateur.id +=1
        self.id = utilisateur.id
        self.nom = nom
        self.password = password
    
