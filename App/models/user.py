from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
db = SQLAlchemy()
import datetime

class User (UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    def toDict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
      }
      
    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username) 