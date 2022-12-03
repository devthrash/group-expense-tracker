from flask import request
from flask_restful import Resource, reqparse
from uuid import uuid4
import os

from ..mongo import mongo


def notify(email: str):
    return