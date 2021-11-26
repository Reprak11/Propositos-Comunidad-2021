from marshmallow import fields
from app.ext import ma
class GoalSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    resume = fields.String()
    goal_one = fields.String()
    goal_two = fields.String()
    goal_three = fields.String()
    contact = fields.String()