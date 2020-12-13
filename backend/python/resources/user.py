from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()
