from .. import db
from ..models import Task
from flask import request
from flask_restful import Resource

class Tasks(Resource):
    def post(self, user_email):
        task = Task({**request.view_args, **request.json})
        db.session.add(task)
        db.session.commit()
        return {'hello': 'test'}
