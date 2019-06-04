from app.models import Matches
import mongoengine
import json

class Match:
    def __init__(self, url):
        self.url = url

    def get(self, skip, limit):
        matches_object = Matches.objects(url__contains=self.url).order_by('-timestamp')
        result = {'count':matches_object.count(), 'results':json.loads(matches_object.skip(skip).limit(limit).to_json())}
        return result

    def create(self, datasouce):
        try:
            target_object = Matches(url=self.url, datasource=datasource).save()
            result = {'result': 'success', 'message':'Added target to DB'}

        except mongoengine.errors.NotUniqueError:
            result = {'result': 'failed', 'message': 'Target already exists'}

        except Exception as e:
            result = {'result': 'failed', 'data': 'Failed to create target'}

        return result