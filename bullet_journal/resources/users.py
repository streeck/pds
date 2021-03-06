from .. import db
from ..models import User
from flask import request
from flask_restful import Resource

class Users(Resource):
    def post(self):
        user = User(request.json)
        db.session.add(user)
        db.session.commit()
        return user.serialize
