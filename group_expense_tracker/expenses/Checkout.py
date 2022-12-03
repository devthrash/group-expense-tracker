from flask import jsonify
from flask_restful import Resource, reqparse

from ..mongo import mongo
from ..authentification import authenticate

parser = reqparse.RequestParser()
parser.add_argument('checked_out', type=bool, required=True)

class Checkout(Resource):
    method_decorators = [authenticate]
    def post(self, uuid):
        params = parser.parse_args()

        query = {'uuid': uuid}

        # check if doc exists
        mongo.expenses.find_one_or_404(query, {'_id': 1})

        # update group
        mongo.expenses.update_one(query, {'$push': {'checked_out': params['checked_out']}})

        return jsonify({
            'results': {'expenses': mongo.expenses.find_one(query,{'_id': 0})['expenses']}
        })