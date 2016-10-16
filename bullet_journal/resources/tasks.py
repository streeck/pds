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


class SingleTask(Resource):
    def patch(self, user_email, task_id):
        task = Task.query.get_or_404(task_id)
        task.done = not task.done
        db.session.add(task)
        db.session.commit()
        return task.serialize

    def delete(self, user_email, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return {}, 200
