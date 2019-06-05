from streaming.config import config
import mongoengine as db
import datetime

db.connect(
    db=config['mongo']['db'],
    host=config['mongo']['host'],
    port=config['mongo']['port']
)

source_options = ('transparency', 'phishtank')
matching_types = ('regex', 'fuzzy')

class Whitelist(db.Document):
    domain = db.StringField(required=True, max_length=500, unique=True)

class Regex(db.Document):
    value = db.StringField(required=True, max_length=500, unique=True)
    score = db.IntField(required=False, default=80)

class Fuzzy(db.Document):
    value = db.StringField(required=True, unique=True)
    likelihood = db.IntField(required=True)
    score = db.IntField(required=False, default=80)

class Matching(db.EmbeddedDocument):
    name = db.StringField(required=True, choices=matching_types)
    value = db.StringField(required=True, max_length=500)
    data = db.DictField()

class Matches(db.Document):
    timestamp = db.DateTimeField(required=False, default=datetime.datetime.now)
    datasource = db.StringField(max_length=50, required=True, choices=source_options)
    matching = db.EmbeddedDocumentField(Matching)

    url = db.StringField(max_length=1000, required=True)
    frequency = db.IntField(required=False, default=900)
    enabled = db.BooleanField(required=False, default=False)

    meta = {
        'ordering': ['-timestamp'],
    }

