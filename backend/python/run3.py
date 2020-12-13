from flask_restful import Resource
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_serialize import FlaskSerializeMixin
from flask_marshmallow import Marshmallow, fields
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@mysql/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)



# Product Class/Model
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(30))
  lastname = db.Column(db.String(30))
  email = db.Column(db.String(40))

  def __init__(self, firstname, lastname, email):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email

# Product Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'email')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/api/')
def hello_world():
    return "Hello World!"


# Get Single User
@app.route('/api/getIndData', methods=['GET'])
def get_user():
    id=request. args. get("id")
    user = User.query.get(id)
    print(id)
    print("##########")
    #return jsonify(user.__dist__)
    return jsonify(user_schema.dump(user))

@app.route('/api/user', methods=['POST'])
def add_user():
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    email = request.json['email']
    new_user = User(firstname, lastname, email)
    db.session.add(new_user)
    db.session.commit()
    #return "new user added"
    return jsonify(user_schema.dump(new_user))

# Update a Product
@app.route('/api/user/<id>', methods=['PUT'])
def update_user(id):
  user = User.query.get(id)

  firstname = request.json['firstname']
  lastname = request.json['lastname']
  email = request.json['email']

  user.firstname = firstname
  user.lastname = lastname
  user.email = email

  db.session.commit()
  #return "user updated successfully"
  return jsonify(user_schema.dump(user))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)