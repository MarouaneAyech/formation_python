import os

basedir = os.getcwd()
db_path=os.path.join(basedir, 'app\data\data.db')

SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'  
SQLALCHEMY_TRACK_MODIFICATIONS = False
Debug = True

# basedir = os.path.abspath(os.path.dirname(__file__))
# os.environ.get('DATABASE_URL')
 #os.environ.get('SECRET_KEY')