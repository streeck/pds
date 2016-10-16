from .. import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer(), primary_key=True)
    user_email = db.Column(db.String(), db.ForeignKey('users.email'))
    text = db.Column(db.String())
    done = db.Column(db.Boolean())

    def __init__(self, request_data):
        self.user_email = request_data['user_email']
        self.text = request_data['text']
        self.done = False
