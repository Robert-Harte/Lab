from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, dotenv_values
import os

DB_NAME = "database.db"

load_dotenv()

db = SQLAlchemy()
DB_STRING = os.getenv('POSTGRES_DB_STRING')

# Initialise the app
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_STRING}"
    #app.config["SECRET_KEY"] = "asjlk;fdsAAHDSFHal;k2345"
    db.init_app(app)
    
    from .views import views
    app.register_blueprint(views, url_prefix="/")
    
    from .models import Pokemon
    with app.app_context():
        db.create_all()
    
    return app