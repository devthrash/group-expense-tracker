from flask import jsonify
from flask_restful import Resource, reqparse

from ..exceptions import InvalidUserEmailException
from ..mongo import mongo
from ..decorators import authenticate

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)


class GroupMembersList(Resource):
    method_decorators = [authenticate]

    def post(self, uuid):
        params = parser.parse_args()

        query = {'uuid': uuid}

        # check if doc exists
        mongo.groups.find_one_or_404(query, {'_id': 1})

        # retrieve user
        user = mongo.users.find_one({'email': params['email']})

        if user is None:
            raise InvalidUserEmailException

        # update group
        mongo.groups.update_one(query, {'$addToSet': {'members': {'email': user['email'], 'name': user['name']}}})

        return jsonify({
            'results': {'members': mongo.groups.find_one(query, {'members': 1})['members']}
        })
