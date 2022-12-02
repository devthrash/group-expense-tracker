import jwt

from flask import jsonify, current_app
from flask_restful import Resource, reqparse

import hashlib

from ..mongo import mongo
from ..exceptions import UnauthorizedException

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)


class Login(Resource):
    def post(self):
        params = parser.parse_args()

        user = mongo.users.find_one({
            'email': params['email'],
            'password': hashlib.sha256(params['password'].encode('utf-8')).hexdigest()
        })

        if user is None:
            raise UnauthorizedException

        jwt_token = jwt.encode({'sub': user['email']}, current_app.config['JWT_SECRET'], algorithm='HS256')

        return jsonify({
            'result': {
                'token': jwt_token.decode('utf-8')
            }
        })
