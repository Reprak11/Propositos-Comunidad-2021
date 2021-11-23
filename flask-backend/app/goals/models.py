from app.db import db, BaseModelMixin
class Goal(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    resume = db.Column(db.String)
    goal-one = db.Column(db.String)
    goal-two = db.Column(db.String)
    goal-three = db.Column(db.String)
    contact = db.Column(db.String)
    def __init__(self, name, resume, goal-one, goal-two, goal-three, contact):
        self.name = name
        self.resume = resume
        self.goal-one = goal-one
        self.goal-two = goal-two
        self.goal-three = goal-three
        self.contact = contact

