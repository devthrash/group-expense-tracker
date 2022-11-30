from flask import Flask, jsonify
from flask_restful import Resource, reqparse

from ..db import mongo

parser = reqparse.RequestParser()
parser.add_argument('name', type="", required=True)
parser.add_argument('email', type="", required=True)
parser.add_argument('password', type="", required=True)
#params = parser.parse_args()

class Authentification(Resource):
    def get(self):
        doc = {
            'menu': 'Authentification',
            'email': 'email',
            'name': 'name',
            'password': 'password'
        }
        
        return jsonify({'result': doc})