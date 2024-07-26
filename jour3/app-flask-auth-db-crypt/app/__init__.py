from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    bcrypt.init_app(app)

    # Associer l'application à la base
    # Créer la base des données

    from .models import User
    with app.app_context():
        db.create_all()
    
    # Associer le blueprint à l'application
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
