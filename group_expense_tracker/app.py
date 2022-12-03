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
    api.add_resource(Expenses, '/api/expenses/')
    api.add_resource(Expense, '/api/expense/<string:uuid>')
    api.add_resource(Checkout, '/api/checkout/<string:uuid>')
    
    @app.route('/notify-expense')
    def notify_expense():
        
        query = {'uuid': request.args.get('group_uuid')}

        # check if doc exists
        mongo.groups.find_one_or_404(query, {'_id': 1})
        
        email_recipients = mongo.groups.find_one(query, {'members': 1})['members']
        
        msg = Message('Hello from the other side!', recipients = email_recipients)
        msg.body = "Someone has added you to a group"
        mail.send(msg)
        return "Message sent!"
        

    return app

    return app
