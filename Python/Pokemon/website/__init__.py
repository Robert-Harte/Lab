from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from sqlaclhemy import create_engine

DB_NAME = "database.db"

db = SQLAlchemy()


# # DEFINE DATABASE DETAILS
# user = 'root'
# password = 'password'
# host = '127.0.0.1'
# port = 5432
# database = pokemon

# def get_connection():
#     return create_engine(
#         url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
#             user, password, host, port, database
#         )
#     )


# Initialise the app
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SECRET_KEY"] = "asjlk;fdsAAHDSFHal;k2345"
    db.init_app(app)
    
    from .views import views
    app.register_blueprint(views, url_prefix="/")
    
    from .models import Pokemon
    with app.app_context():
        db.create_all()
    
    return app