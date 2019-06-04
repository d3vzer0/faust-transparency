from streaming.config import config
import mongoengine as db
import datetime

db.connect(
    db=config['mongo']['db'],
    host=config['mongo']['host'],
    port=config['mongo']['port']
)

class Responses(db.EmbeddedDocument):
    response_code = db.IntField(required=False)
    response_data = db.StringField(required=False)

class Snapshots(db.Document):
    url = db.StringField(max_length=1000, required=True)
    timestamp = db.DateTimeField(required=False, default=datetime.datetime.now)
    response = db.EmbeddedDocumentField(Responses)
    sha256 = db.StringField(max_length=256, required=True)
    screenshot = db.FileField()

    meta = {
        'ordering': ['-timestamp'],
    }
