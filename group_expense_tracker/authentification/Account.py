from flask import jsonify
from flask_restful import Resource

from ..db import mongo


class Account(Resource):
    def get(self, email):
        return jsonify({'result': mongo.authentification.find_one_or_404({'email': email}, {'_id': 0})})
