from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from pykafka import KafkaClient

# Initialize Flask Instance and load configuration
app = Flask(__name__)
from  app.configs import *

# Initialize DB and load models and views
api = Api(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})
db = MongoEngine(app)

# Initialise Kafka client connection for filter updates
kafka_client = KafkaClient(hosts=app.config['KAFKA_HOST'])
client_topic = kafka_client.topics['wordmatching-update']
producer = client_topic.get_producer()

# Import views
from app import api_generic
from app import api_matches
from app import api_snapshots
from app import api_filters
