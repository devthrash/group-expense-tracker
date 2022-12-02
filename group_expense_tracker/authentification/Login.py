import jwt

from flask import jsonify
from flask_restful import Resource, reqparse

import hashlib

from ..db import mongo
from ..exceptions import UnauthorizedException

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)


class Login(Resource):
    def __init__(self, **kwargs):
        self._secret = kwargs['secret']

    def post(self):
        params = parser.parse_args()

        user = mongo.users.find_one({
            'email': params['email'],
            'password': hashlib.sha256(params['password'].encode('utf-8')).hexdigest()
        })

        if user is None:
            raise UnauthorizedException

        return jsonify({
            'result': {
                'token': jwt.encode({'sub': user['email']}, self._secret, algorithm='HS256').decode('utf-8')
            }
        })
