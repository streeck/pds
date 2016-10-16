from .. import db
from ..models import User, Task
from flask import request
from flask_restful import Resource

class Tasks(Resource):
    def post(self, user_email):
        task = Task({**request.view_args, **request.json})
        db.session.add(task)
        db.session.commit()
        return {'hello': 'test'}

    def get(self, user_email):
        user = User.query.get_or_404(user_email)
        return {'tasks': [i.serialize for i in user.tasks]}
