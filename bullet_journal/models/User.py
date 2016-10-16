from .. import db
from sqlalchemy.dialects.postgresql import ARRAY

class User(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(), primary_key=True)
    facebook_id = db.Column(db.String(), unique=True)
    friends = db.Column(ARRAY(db.String()))
    sharing = db.Column(db.Boolean())
    tasks = db.relationship('Task', backref='user', lazy='dynamic')

    def __init__(self, request_data):
        self.email = request_data['email']
        self.facebook_id = request_data['facebook_id']
        self.friends = request_data['friends']
        self.sharing = request_data['sharing']

    @property
    def serialize(self):
       return {
           'email': self.email,
           'facebook_id': self.facebook_id,
           'friends': self.friends,
           'sharing': self.sharing
       }
