# Setting variables
from app import app
import os

# Todo - set MongoDB username and Password as variables for DB
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET')
app.config['FLASK_PORT'] = int(os.getenv('FLASK_PORT', 5000))
app.config['CORS_DOMAIN'] = os.getenv('CORS_DOMAIN', '*')
app.config['KAFKA_HOST'] = os.getenv('KAFKA_HOST', 'localhost:29092')
app.config['MONGODB_SETTINGS'] = {
    'db': 'phishyme',
    'host': os.getenv('DBHOST', 'localhost'),
    'port': os.getenv('DBPORT', 27017)
}
