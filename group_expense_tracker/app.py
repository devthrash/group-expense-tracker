from flask import Flask, jsonify
from flask_restful import Api

from .db import mongo
from .groups.Group import Group
from .groups.Groups import Groups


def create_app(config):
    app = Flask(__name__)
    app.config['MONGO_URI'] = config['DB_URI']

    @app.route('/')
    def hello_world():
        mongo.test_collection.update_one({'hello': 'world'}, {"$set": {'hello': 'world'}}, upsert=True)

        return jsonify(mongo.test_collection.find_one({'hello': 'world'}, {'_id': 0}))

    api = Api(app)
    api.add_resource(Group, '/api/groups/<string:uuid>')
    api.add_resource(Groups, '/api/groups')

    return app
