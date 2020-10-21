from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/testdb'
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
  qty = db.Column(db.Integer)

  def __init__(self, firstname, lastname, email):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email

# Product Schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'firstname', 'lastname', 'email')

# Init schema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)

@app.route('/api/')
def add_user01():
    print("testing...")
    return "hellow"

@app.route('/api/user/test/', methods=['GET'])
def add_user00():
    print("testing...")
    return "hellow"

# Create a Product
@app.route('/api/user/add/', methods=['POST'])
def add_user():
    print("adding user")
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    email = request.json['email']
    
    new_user = User(firstname, lastname, email)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

# Get All Products
@app.route('/api/user/get/', methods=['GET'])
def get_user1():
    all_user = User.query.all()
    result = user_schema.dump(all_user)
    return jsonify(result.data)

# Get Single Products
@app.route('/api/user/get/<id>', methods=['GET'])
def get_user2(id):
  user = User.query.get(id)
  return user_schema.jsonify(user)

# Update a Product
@app.route('/api/user/update/<id>', methods=['PUT'])
def update_product3(id):
  user = User.query.get(id)

  firstname = request.json['firstname']
  lastname = request.json['lastname']
  email = request.json['email']

  user.firstname = firstname
  user.lastname = lastname
  user.email = email

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/user/delete/<id>', methods=['DELETE'])
def delete_user4(id):
  user = User.query.get(id)
  db.session.delete(user)
  db.session.commit()

  return user_schema.jsonify(user)

# Run Server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)