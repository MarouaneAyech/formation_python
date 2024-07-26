from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
dash_application = None

def create_app():
    global dash_application

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    bcrypt.init_app(app)

    migrate = Migrate(app, db)
    from .models import User, Produit

    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    from .dash_app.app import create_dash_app
    dash_application=create_dash_app(app)

    return app

