from flask import request, Blueprint
from flask_restful import Api, Resource
from .schemas import GoalSchema
from ..models import Goal

goals_v1_0_bp = Blueprint('goals_v1_0_bp', __name__)
goal_schema = GoalSchema()
api = Api(goals_v1_0_bp)

class GoalListResource(Resource):
    def get(self):
        goals = Goal.get_all()
        if goals is None:
            raise ObjectNotFound('No hay usuarios')
        result = goal_schema.dump(films, many=True)
        return result

class GoalAddResource(Resource):
    def post(self):
        data = request.get_json()
        goal_dict = goal_schema.load(data)
        goal = Goal(name=goal_dict['name'],
                    resume=goal_dict['resume'],
                    goal_one=goal_dict['goal_one'],
                    goal_two=goal_dict['goal_two'],
                    goal_three=goal_dict['goal_three'],
                    contact=goal_dict['contact']
        )
        goal.save()
        resp = goal_schema.dump(film)
        return resp, 201

api.add_resource(GoalListResource, '/api/v1.0/goals/', endpoint='goals_resource')
api.add_resource(GoalAddResource, '/api/v1.0/addgoal/', endpoint='addgoal_resource')