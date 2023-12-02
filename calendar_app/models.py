from flask_sqlalchemy import SQLAlchemy

from . import app

import os

abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{abs_path}/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Integer, nullable=False)  # YYYYMMDD (8 digit integer)
    start_time = db.Column(db.Integer)  # HHMM (4 digit integer, 24 hour format)
    end_time = db.Column(db.Integer)  # HHMM (4 digit integer, 24 hour format)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    done = db.Column(db.Boolean)

with app.app_context():
    db.create_all()
