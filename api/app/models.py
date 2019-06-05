from app import db
import datetime

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


class RevokedTokens(db.Document):
    token = db.StringField(max_length=150, required=True, unique=True)

class Users(db.Document):
    username = db.StringField(max_length=50, required=True, unique=True)
    password = db.StringField(max_length=128, required=True)
    salt = db.StringField(required=True, max_length=128)