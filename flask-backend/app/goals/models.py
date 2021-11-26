from app.db import db, BaseModelMixin
class Goal(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    resume = db.Column(db.VARCHAR(255))
    goal_one = db.Column(db.VARCHAR(255))
    goal_two = db.Column(db.VARCHAR(255))
    goal_three = db.Column(db.VARCHAR(255))
    contact = db.Column(db.VARCHAR(255))
    def __init__(self, name, resume, goal_one, goal_two, goal_three, contact):
        self.name = name
        self.resume = resume
        self.goal_one = goal_one
        self.goal_two = goal_two
        self.goal_three = goal_three
        self.contact = contact

