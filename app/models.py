from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Player(UserMixin, db.Model):
    __tablename__ = 'player'
    id_user     = db.Column(db.Integer, primary_key = True)
    nama        = db.Column(db.String(50), nullable = False)
    jk          = db.Column(db.String(1), nullable = False)
    tgllahir    = db.Column(db.DateTime, default = datetime.utcnow)
    email       = db.Column(db.String(50), nullable = False, unique = True)
    latitude    = db.Column(db.Float(15), nullable = False)
    longitude   = db.Column(db.Float(15), nullable = False)
    username    = db.Column(db.String(30), nullable = False, unique = True)
    password    = db.Column(db.String(255))

    def __repr__(self):
        return '<Username {}>'.format(self.username)
    
    def hash_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)