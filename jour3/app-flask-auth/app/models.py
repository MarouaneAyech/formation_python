# Définition des modèles de données (par exemple, User)
class User:
    def __init__(self, nom, login, password, ville):
        self.nom = nom
        self.login = login
        self.password = password
        self.ville = ville
