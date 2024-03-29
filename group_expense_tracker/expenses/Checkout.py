from flask import jsonify
from flask_restful import Resource, reqparse

from ..mongo import mongo
from ..decorators import authenticate

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
        mongo.expenses.update_one(query, {'$set': {'checked_out': params['checked_out']}})
        mongo.groups.update_one({
            'expenses.uuid': uuid
        }, {
            '$set': {'expenses.$.checked_out': params['checked_out']}
        })

        return jsonify({
            'results': {'expenses': mongo.expenses.find_one(query,{'_id': 0})}
        })
