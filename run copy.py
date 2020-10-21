from flask import Flask
from flask import request
from flask import jsonify 
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)                             


SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/testdb'

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# db variable initialization
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(30), nullable=True)
    lastname=db.Column(db.String(30), nullable=True)
    email=db.Column(db.String(50), nullable=True)


    def __repr__(self):
        return "<User: {}>".format(self.firstname)

@app.route('/api/')                                   
def hello_world():                                
    return "Hello World!"                         

@app.route("/api/add/", methods=["POST"])
def home():
    print("adding user is called")
    user = User(firstname=request.form.get("firstname"),lastname=request.form.get("lastname"),email=request.form.get("email"))
    db.session.add(user)
    db.session.commit()
    return "inserted"


if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=5000, debug=True)