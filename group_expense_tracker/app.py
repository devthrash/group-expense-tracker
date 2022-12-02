from flask import Flask
from flask_restful import Api

from .authentification.Login import Login
from .groups.Group import Group
from .groups.Groups import Groups
from .groups.GroupMembers import GroupMembers
from .users.UsersList import UsersList
from .users.User import User


def create_app(config):
    app = Flask(__name__)
    app.config['MONGO_URI'] = config['DB_URI']

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

    api.add_resource(Login, '/api/auth', resource_class_kwargs={'secret': config['JWT_SECRET']})
    api.add_resource(Groups, '/api/groups')
    api.add_resource(Group, '/api/groups/<string:uuid>')
    api.add_resource(GroupMembers, '/api/groups/<string:uuid>/members')
    api.add_resource(UsersList, '/api/users')
    api.add_resource(User, '/api/users/<string:uuid>')

    return app
