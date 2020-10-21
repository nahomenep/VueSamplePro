from flask import Flask, render_template
from flask import request
from flask import jsonify  
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow 
from flask_mysqldb import MySQL
import yaml
#from user_controller import UserController

class Application:
    def __init__(self, app):
        self.app = app
        self.db = MySQL(self.app)                                   
 #       self.user_controller = UserController(self.db)

    def run(self):
        print("Starting application ")
        self.app.run(host="0.0.0.0", port=5000, debug=True)
        self.app.add_url_rule("/api/", "Home", self.hello_world)
        self.app.add_url_rule("/api/users", "New User", self.add_user)        

    def hello_world(self):                                
        return "Hello World!"   

    def add_user(self):
        self.user_controller.add_user()

app = Flask(__name__)
if __name__ == '__main__':
    print("######## Application instance####### \n\n\n")
    application = Application(app)                     
    application.run()