from flask import Flask, jsonify
from flask_restful import Resource, reqparse

from ..db import mongo

parser = reqparse.RequestParser()
parser.add_argument('name', type= str, required=True)
parser.add_argument('email', type= str, required=True)
parser.add_argument('password', type= str, required=True)
parser.add_argument('reinsert_password', type= str, required=True)

#Initial state
doc = {
    'email': 'Insert account email here',
    'name': 'Insert account name here',
    'password': 'Insert account password here',
    'reinsert_password': 'Reinsert password please'
}

class Authentification(Resource):
    #Print
    def get(self) :        
        return jsonify({'Authentication': doc})
    
    #Insert credentials 
    def post(self) :        
        email = parser.parse_args()
        name = parser.parse_args()
        password = parser.parse_args()
        reinsert_password = parser.parse_args()
        doc = {
        'email': email,
        'name': name,
        'password': password,
        'reinsert_password': reinsert_password
    }
        return jsonify({'Authentication': doc})