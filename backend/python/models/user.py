from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy, Model,
from flask_marshmallow import Marshmallow 

class User(Model):
    id = Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    email = db.Column(db.String(40))
    
    def __init__(self):
        pass