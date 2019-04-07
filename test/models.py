from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from test import app, login

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(16), nullable=False, server_default='', unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash=db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) # default method='pbkdf2:sha256'

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def repr(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

