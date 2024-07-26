from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask import session
from . import db
from .models import User, Produit
from . import bcrypt
from .validation import login_required
import pandas as pd
# from .pipeline.transformers import extract_month

main_bp = Blueprint('main', __name__)

##########################
from flask import Flask, jsonify, request
import pickle
# Charger le modèle sauvegardé
import os
###########################"

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
            session['user'] = {'nom': user.nom, 'login': user.login}
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

@main_bp.route("/produit", methods=["GET", "POST"])
@login_required
def produit():
    if request.method == "POST":
        nom = request.form.get("nom")
        categorie = request.form.get("categorie")

        new_produit = Produit(nom=nom, categorie=categorie)
        db.session.add(new_produit)
        db.session.commit()

        produits = Produit.query.all()
        return render_template("produits_table.html", produits=produits)

    produits = Produit.query.all()
    return render_template("produit.html", produits=produits)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    from . import dash_application
    from .dash_app.app import load_dash_app_layout
    dash_application=load_dash_app_layout(dash_application)
    dash_layout = dash_application.index()
    return render_template('dashboard.html', dash_layout=dash_layout)

@main_bp.route('/home', methods=['GET'])
@login_required
def home():
    user = User(**session['user'], password=" ", ville=" ") 
    return render_template('login_success.html' , user=user)

@main_bp.route('/predict', methods=['POST'])
def predict():
    # # Récupérer les données JSON envoyées avec la requête POST
    # data = request.get_json()
    # # Vérifier si les données attendues sont présentes dans la requête
    # if 'nom' not in data or 'categorie' not in data or 'puht' not in data and 'quantite_vendue' not in data:
    #     return jsonify({'prediction':None}), 400
    # # Exemple : Si les données sont dans un format spécifique 'x', faire une prédiction
    # nom = data['nom']  # Adapter selon votre format de données
    # categorie = data['categorie']
    # puht = data['puht']
    # date = data['date']
    # quantite_vendue = data['quantite_vendue']
    # # Faire une prédiction avec le modèle chargé
    # df_vente=pd.DataFrame([{
    # "puht": puht,
    # "quantite_vendue": quantite_vendue,
    # "date" : date,
    # "categorie": categorie,
    # "nom": nom}])
    
     # Récupérer les données JSON envoyées avec la requête POST
    data = request.get_json()
    
    # Vérifier si les données sont présentes
    if 'data' not in data:
        return jsonify({'predictions': None}), 400
    
    # Convertir les données JSON en DataFrame
    df = pd.DataFrame(data['data'])

    # from .pipeline.transformers import extract_month
    data_dir =  os.path.join(os.path.dirname(os.path.abspath(__file__)),'pipeline')
    pipeline_path=os.path.join(data_dir,'pipeline.pkl')
    import dill
    with open(pipeline_path, 'rb') as f:
        pipeline = dill.load(f)
    prediction = pipeline.predict(df)
    # Retourner la prédiction sous forme de JSON
    return jsonify({'prediction': prediction.tolist()})