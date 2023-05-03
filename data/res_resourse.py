from flask_restful import Resource
from data import db_session
from data.rating import Rating
from flask import abort, jsonify
from data.user_parse import parser
from werkzeug.security import generate_password_hash


class RatListResource(Resource):
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = Rating()
        user.nickname = args['nickname']
        user.result = args['result']
        session.add(user)
        session.commit()