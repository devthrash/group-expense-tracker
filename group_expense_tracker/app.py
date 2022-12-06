from email.message import Message
from flask import Flask,request
from flask_restful import Api
from flask_mail import Mail

from .mongo import mongo

from .authentification.Login import Login
from .groups.Group import Group
from .groups.GroupsList import GroupsList
from .groups.GroupMembersList import GroupMembersList
from .users.UsersList import UsersList
from .users.User import User
from .expenses.Expense import Expense
from .expenses.Expenses import Expenses
from .expenses.Checkout import Checkout
from .expenses.Notify import Notify


def create_app(config):
    app = Flask(__name__)
    app.config['MONGO_URI'] = config['DB_URI']
    app.config['JWT_SECRET'] = config['JWT_SECRET']
    app.config['MAIL_SERVER'] = config['MAIL_SERVER']
    app.config['MAIL_PORT'] = config['MAIL_PORT']
    app.config['MAIL_USERNAME'] = config['MAIL_USERNAME']
    app.config['MAIL_PASSWORD'] = config['MAIL_PASSWORD']
    app.config['MAIL_USE_TLS'] = config['MAIL_USE_TLS']

    errors = {
        'UnauthorizedException': {
            'message': "Unauthorized",
            'status': 401,
        },
        'EmailAlreadyRegistered': {
            'message': 'Email is already in use',
            'status': 400
        },
        'InvalidUserEmailException': {
            'message': 'Invalid user email',
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
    api.add_resource(Expenses, '/api/expenses/')
    api.add_resource(Expense, '/api/expense/<string:uuid>')
    api.add_resource(Checkout, '/api/checkout/<string:uuid>')
    api.add_resource(Notify, '/api/notify/<string:uuid>')
        
    return app