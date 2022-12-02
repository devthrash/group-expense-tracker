from flask import jsonify, g
from flask_restful import Resource, reqparse
from uuid import uuid4

from ..mongo import mongo
from ..decorators import authenticate

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('members', type=str, required=True, action='append')


class GroupsList(Resource):
    method_decorators = [authenticate]

    def get(self):
        docs = [doc for doc in mongo.groups.find({'created_by': g.logged_in_user}, {'_id': 0})]

        return jsonify({
            'results': {'groups': docs}
        })

    def post(self):
        creator_email = g.logged_in_user
        params = parser.parse_args()

        doc = {
            'uuid': str(uuid4()),
            'name': params['name'],
            'members': [
                {'email': creator_email, 'name': 'Test Testulescu'}
            ],
            'expenses': [],
            'created_by': creator_email
        }

        for email in params['members']:
            # todo read from users/accounts collection or whatever
            doc['members'].append({'email': email, 'name': 'Nume'})

        mongo.groups.insert_one(doc)

        doc.pop('_id', None)
        return jsonify({'result': doc})