from marshmallow import fields
from app.ext import ma
class GoalSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    resume = fields.String()
    goal-one = fields.String()
    goal-two = fields.String()
    goal-three = fields.String()
    contact = fields.String()