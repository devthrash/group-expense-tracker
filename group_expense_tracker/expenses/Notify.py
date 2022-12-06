from flask import request, current_app, g
from flask_restful import Resource, reqparse
from uuid import uuid4
from flask_mail import Mail, Message

from ..decorators import authenticate

from ..mongo import mongo


class Notify(Resource):
    method_decorators = [authenticate]
    
    def post(self, uuid):
        query = {'uuid': uuid}
        
        print(mongo.groups.find_one_or_404(query, {'_id': 1}))
        
        # members = mongo.groups.find_one(query, {'_id': 1})['members']
        # app = current_app._get_current_object()
        # with app.app_context():
        #     mail = Mail(app=app)
        #     for member in members:
        #         msg = Message('Hello from Group Expense Tracker!', recipients = member['email'])
        #         msg.body = "Hey ()! There is a new expense waiting for you to be checked out!".format(member['name'])
        #         mail.send(msg)


        