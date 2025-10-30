from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "database.db"

db = SQLAlchemy()


# DEFINE DATABASE DETAILS
user = 'postgres'
password = 'mypassword'
host = 'host.docker.internal'
port = 5432
database = "pokemon"

# Initialise the app
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    #app.config["SECRET_KEY"] = "asjlk;fdsAAHDSFHal;k2345"
    db.init_app(app)
    
    from .views import views
    app.register_blueprint(views, url_prefix="/")
    
    from .models import Pokemon
    with app.app_context():
        db.create_all()
    
    return app