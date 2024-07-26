from . import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    ville = db.Column(db.String(100))

    def __init__(self, nom, login, password, ville):
        self.nom = nom
        self.login = login
        self.set_password(password)  # hashage de mot de passe
        self.ville = ville

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class Produit(db.Model):
    __tablename__ = 'produit'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    categorie = db.Column(db.String(50))

    def __init__(self, nom, categorie):
        self.nom = nom
        self.categorie = categorie