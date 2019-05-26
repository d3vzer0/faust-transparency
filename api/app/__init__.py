from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_cors import CORS

#Initialize Flask Instance
app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

# Initialize DB and load models and views
from  app.configs import *
CORS(app, resources={r"*": {"origins": "*"}})
db = MongoEngine(app)

# Import views
from app import api_search
