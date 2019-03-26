from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from test import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(16), nullable=False, server_default='', unique=True)
    password_hash=db.Column(db.String(128))

    def repr(self):
        return '<User {}>'.format(self.username)



