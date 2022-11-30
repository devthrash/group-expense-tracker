from flask import jsonify
from flask_restful import Resource, reqparse

from ..db import mongo

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)


class GroupMembers(Resource):
    def post(self, uuid):
        params = parser.parse_args()

        query = {'uuid': uuid}

        # check if doc exists
        mongo.groups.find_one_or_404(query, {'_id': 1})

        # update group
        mongo.groups.update_one(query, {'$push': {'members': {'email': params['email'], 'name': 'Nume'}}})

        return jsonify({
            'results': {'members': mongo.groups.find_one(query, {'members': 1})['members']}
        })
