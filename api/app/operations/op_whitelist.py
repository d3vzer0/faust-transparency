from app.models import Whitelist as DBWhitelist
import mongoengine
import json


class Whitelist:
    def __init__(self, value):
        self.value = value
    
    def get(self):
        objects = DBWhitelist.objects()
        result = {'count':objects.count(), 'data':json.loads(objects.to_json())}
        return result

    def create(self):
        try:
            filter = DBWhitelist(domain=self.value).save()
            result = {'result': 'created', 'message': 'Succesfully added domain to whitelist'}

        except mongoengine.errors.NotUniqueError:
            result = {'result': 'failed', 'message': 'Domain already exists in whitelist'}

        except Exception as err:
            result = {'result': 'failed', 'message': 'Failed to add domain to whitelist'}

        return result 


    def delete(self):
        try:
            filter_object = DBWhitelist.objects.get(domain=self.value).delete()
            result = {'result': 'deleted', 'message': 'Deleted domain from whitelist'}

        except mongoengine.errors.DoesNotExist:
            result = {'result': 'failed', 'message': 'Domain does not exist in whitelist'}

        except Exception as err:
            result = {'result': 'failed', 'message': 'Failed to delete domain from whitelist'}

        return result
