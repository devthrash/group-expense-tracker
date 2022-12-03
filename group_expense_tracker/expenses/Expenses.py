from flask import jsonify, redirect, url_for
from flask_restful import Resource, reqparse
from uuid import uuid4

from ..mongo import mongo

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('cost', type=int, required=True)
parser.add_argument('group', type=str, required=False)


class Expenses(Resource):
    def get(self):
        creator_email = 'test@example.com'

        docs = [doc for doc in mongo.expenses.find({'created_by': creator_email}, {'_id': 0})]

        return jsonify({
            'results': {'expenses': docs}
        })
        
    def post(self):
        creator_email = 'test@example.com'
        params = parser.parse_args()

        doc = {
            'uuid': str(uuid4()),
            'name': params['name'],
            'cost': params['cost'],
            'group': params['group'],
            'checked_out': False,
            'created_by': creator_email
        }

        if any in doc['group']:
            self.send_notification(doc['group'])
            
        mongo.expense.insert_one(doc)

        doc.pop('_id', None)
        return jsonify({'result': doc})
    
    def send_notification(group_name):
        query = {'name': group_name}
        
        group_uuid = mongo.groups.find_one(query, {'_id': 1})['uuid']
        return redirect(url_for('notify', group_uuid = group_uuid))