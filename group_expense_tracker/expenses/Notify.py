from flask import current_app, jsonify
from flask_restful import Resource, reqparse
from uuid import uuid4
from flask_mail import Mail, Message

import json

from .. import app

from ..decorators import authenticate

from ..mongo import mongo

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)

class Notify(Resource):
    method_decorators = [authenticate]
    
    def post(self):
        params = parser.parse_args()
        query = {'name': params['name']}
        
        members = mongo.groups.find_one(query)['members']
        
        app = current_app._get_current_object()
        with app.app_context():
            mail = Mail(app=app)
            for member in members:
                msg = Message('Hello from Group Expense Tracker!', sender= app.config['MAIL_USERNAME'], recipients= [member['email']])
                msg.body = "Hey! There is a new expense waiting for you to be checked out!"
                mail.send(msg)
        
        return jsonify({'result': mongo.groups.find_one_or_404(query, {'_id': 0})})


        