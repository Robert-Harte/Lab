from . import db
from sqlalchemy.sql import func

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    number = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    type = db.Column(db.String(150))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())