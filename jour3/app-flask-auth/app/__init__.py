from flask import Flask
# Importer et enregistrer les blueprints
from .routes import main_bp

def create_app():
    app = Flask(__name__)

    # Charger la configuration de l'application (si nécessaire)
    app.config.from_pyfile('config.py')


    app.register_blueprint(main_bp)

    return app
