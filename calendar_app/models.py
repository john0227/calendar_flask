from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Schedule(db.Model):
    sch_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sch_name = db.Column(db.String(255), nullable=False)
    sch_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(255))
    done = db.Column(db.Boolean)
