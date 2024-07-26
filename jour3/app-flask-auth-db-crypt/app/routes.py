from flask import Blueprint, render_template, request, redirect, url_for
from flask import session
from . import db
from .models import User
from . import bcrypt

main_bp = Blueprint('main', __name__)

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
        # user = User.query.filter_by(login=login, password=password).first()
        # if user:
        user = User.query.filter_by(login=login).first()
        if user and user.check_password(password):
            session['user'] = {'id': user.id, 'nom': user.nom, 'login': user.login}
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
        existing_user = User.query.filter_by(login=login).first()
        if existing_user:
            return render_template("register.html", error="Ce login existe déjà !!")  
        new_user = User(nom=nom, login=login, password=password, ville=ville)
        db.session.add(new_user)
        db.session.commit()
        return render_template("register_success.html", user=new_user)
    return render_template("register.html")

# Déconnexion
@main_bp.route("/logout")
def logout():
    session.pop('user', None)  # Supprimer l'utilisateur de la session
    return redirect(url_for('main.login'))
