from flask import jsonify
from flask_restful import Resource

from ..mongo import mongo


class Expense(Resource):
    def get(self, uuid):
        return jsonify({'result': mongo.expense.find_one_or_404({'uuid': uuid}, {'_id': 0})})
    