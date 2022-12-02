from functools import wraps

import jwt
from flask import request, g

from .exceptions import UnauthorizedException


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization', None)

        if token is None:
            raise UnauthorizedException

        try:
            decoded = jwt.decode(token.replace('Bearer ', ''), 'secret', algorithms=['HS256'])  # @todo read secret from config
        except jwt.DecodeError:
            raise UnauthorizedException

        g['logged_in_user'] = decoded['sub']  # @todo clear this value after request is finished
        return func(*args, **kwargs)

    return wrapper
