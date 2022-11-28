from flask import jsonify
from flask_restful import Resource, reqparse
from uuid import uuid4

from ..db import mongo

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('users', type=str, required=True, action='append')


class Groups(Resource):
    def post(self):
        params = parser.parse_args()

        doc = {'uuid': str(uuid4()), 'name': params['name'], 'users': []}

        for user in params['users']:
            # todo read from users/accounts collection or whatever
            doc['users'].append(user)

        mongo.groups.insert_one(doc)

        return jsonify({'result': {'uuid': doc['uuid']}})
