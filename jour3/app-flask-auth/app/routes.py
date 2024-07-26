from flask import Blueprint, render_template, request, redirect, url_for
from .models import User

main_bp = Blueprint('main', __name__)

# Liste des utilisateurs (simulation de base de données)
users = []

# Route principale, redirige automatiquement vers /login
@main_bp.route("/")
def index():
    return redirect(url_for('main.login'))

# Page de login
@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        # Vérification simple pour l'exemple
        for user in users:
            if user.login == login and user.password == password:
                return render_template("login_success.html", user=user)
        
        return render_template("login.html", error="Login ou mot de passe incorrect")

    return render_template("login.html")

# Page d'inscription
@main_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nom = request.form.get("nom")
        login = request.form.get("login")
        password = request.form.get("password")
        ville = request.form.get("ville")

        # Vérifier si le login existe déjà
        for user in users:
            if user.login == login:
                return render_template("register.html", error="Ce login existe déjà, veuillez choisir un autre.")

        # Création d'un nouvel utilisateur et ajout à la liste
        new_user = User(nom, login, password, ville)
        users.append(new_user)

        return render_template("register_success.html", user=new_user)

    return render_template("register.html")

# Déconnexion
@main_bp.route("/logout")
def logout():
    return redirect(url_for('main.login'))
