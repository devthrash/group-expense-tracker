from flask import Flask
from flask_restful import Api

from .authentification.Login import Login
from .groups.Group import Group
from .groups.GroupsList import GroupsList
from .groups.GroupMembersList import GroupMembersList
from .users.UsersList import UsersList
from .users.User import User


def create_app(config):
    app = Flask(__name__)
    app.config['MONGO_URI'] = config['DB_URI']
    app.config['JWT_SECRET'] = config['JWT_SECRET']

    errors = {
        'UnauthorizedException': {
            'message': "Unauthorized",
            'status': 401,
        },
        'EmailAlreadyRegistered': {
            'message': 'Email is already in use',
            'status': 400
        }
    }

    api = Api(app, errors=errors)

    api.add_resource(Login, '/api/auth')
    api.add_resource(GroupsList, '/api/groups')
    api.add_resource(Group, '/api/groups/<string:uuid>')
    api.add_resource(GroupMembersList, '/api/groups/<string:uuid>/members')
    api.add_resource(UsersList, '/api/users')
    api.add_resource(User, '/api/users/<string:uuid>')

    return app
