from flask import Flask

#from . database import Database
#from . user import User
import pathlib
from .user_controller import UserController
app = Flask(__name__)            

#db = Database(app)

#userController = UserController(db)

@app.route('/api/')
def hello_world():                                
    return "Hello World!"                         

@app.route("/api/add/", methods=["POST"])
def home():
    #user = User()
    #userController.add_user(user)
    return "User added"


if __name__ == '__main__':
    print("path.....\n")
    print(pathlib.Path(__file__).parent.absolute())
    app.run(host="0.0.0.0", port=5000, debug=True)