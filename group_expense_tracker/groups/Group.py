from flask import jsonify
from flask_restful import Resource

from ..mongo import mongo
from ..decorators import authenticate


class Group(Resource):
    method_decorators = [authenticate]

    def get(self, uuid):
        return jsonify({'result': mongo.groups.find_one_or_404({'uuid': uuid}, {'_id': 0})})
