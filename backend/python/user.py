from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy, Model
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, String


class User(Model):
    id = Column(Integer, primary_key = True)
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(40))
    
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname  = lastname
        self.email = email
