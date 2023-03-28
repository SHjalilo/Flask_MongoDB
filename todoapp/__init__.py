from flask import Flask 

from .main.routes import main
#from todoapp.main.routes import main
from .extentions import mongo


def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] ='mongodb+srv://abdjalile:Aoukane.19@cluster0.0sebbyh.mongodb.net/?retryWrites=true&w=majority'
    mongo.init_app(app)

    
    app.register_blueprint(main)

    return app

#main.run(host= '0.0.0.0', debug=True)