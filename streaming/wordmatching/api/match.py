from streaming.wordmatching.api.models import Matches, Matching
import mongoengine

class Match:
    def __init__(self, url):
        self.url = url

    async def create(self, datasource, variant, value, data=None):
        try:
            match_source = Matching(name=variant, value=value, data=data)
            target_object = Matches( url=self.url, datasource=datasource, matching=match_source).save()
            result = {'result':'success', 'message':'Succesfully added match to DB'}

        except mongoengine.errors.NotUniqueError:
            result = {'result': 'failed', 'message': 'Target already exists'}

        except Exception as e:
            result = {'result': 'failed', 'data': 'Failed to create target'}

        return result
