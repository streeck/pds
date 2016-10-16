import os
from flask import Flask, g, jsonify
from flask_restful import Api
from . import db
from flask_cors import CORS
from datetime import datetime
from .resources import Users, Tasks, SingleTask


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    db.init_app(app)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uwrhjjryckxmna:_IpSDyE7t4_qRE_3girJixibCP@ec2-54-235-68-4.compute-1.amazonaws.com:5432/d4v8pka5tur8fs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/bullet_journal'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TIMESTAMP_FORMAT'] = '%Y-%m-%d %H:%M:%S'

    @app.before_request
    def before_request():
        g.timestamp = datetime.now().strftime(app.config['TIMESTAMP_FORMAT'])

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'message': 'The requested URL was not found on the server.'}), 404

    api.add_resource(Users, '/users/', endpoint='users')

    api.add_resource(Tasks, '/users/<string:user_email>/tasks/', endpoint='tasks')
    api.add_resource(SingleTask, '/users/<string:user_email>/tasks/<int:task_id>', endpoint='task')

    return app
