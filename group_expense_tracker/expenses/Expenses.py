from flask import jsonify, redirect, url_for, g
from flask_restful import Resource, reqparse
from uuid import uuid4

from ..decorators import authenticate

from ..mongo import mongo

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('cost', type=int, required=True)
parser.add_argument('group', type=str, required=False)


class Expenses(Resource):
    method_decorators = [authenticate]
    
    def get(self):
        creator_email = g.logged_in_user

        docs = [doc for doc in mongo.expenses.find({'created_by': creator_email}, {'_id': 0})]

        return jsonify({
            'results': {'expenses': docs}
        })
        
    def post(self):
        creator_email = g.logged_in_user
        params = parser.parse_args()

        doc = {
            'uuid': str(uuid4()),
            'name': params['name'],
            'cost': params['cost'],
            'group': params['group'],
            'checked_out': False,
            'created_by': creator_email
        }

        mongo.expenses.insert_one(doc)
        doc.pop('_id', None)

        if doc['group']:
            group_name = doc['group']
            query = {'name': group_name}
            doc.pop('group')
            mongo.groups.update_one(query, {'$push': {'expenses':doc}})
            #self.send_notification(group_name)
        
        return jsonify({'result': doc})
    
    def send_notification(group_name):
        return redirect(url_for('notify', group_name = group_name))