from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mongoengine import MongoEngine

# Initialize Flask Instance and load configuration
app = Flask(__name__)
from  app.configs import *

# Initialize DB and load models and views
api = Api(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})
db = MongoEngine(app)

# Import views
from app import api_generic
from app import api_matches
from app import api_snapshots
from app import api_filters
