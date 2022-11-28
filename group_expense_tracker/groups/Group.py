from flask import jsonify
from flask_restful import Resource

from ..db import mongo


class Group(Resource):
    def get(self, uuid):
        return jsonify({'result': mongo.groups.find_one_or_404({'uuid': uuid}, {'_id': 0})})
