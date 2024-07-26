from . import db ,  bcrypt

class User(db.Model):
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
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


