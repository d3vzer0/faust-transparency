from app.models import Fuzzy
import mongoengine

class Fuzzy:
    def __init__(self, value):
        self.value = value
    
    def create(self, likelihood, score=None):
        try:
            filter = Fuzzy(value=self.value, likelihood=likelihood, score=score).save()
            result = {"result": "created", "message": "Succesfully created filter"}

        except mongoengine.errors.NotUniqueError:
            result = {"result": "failed", "message": "Filter already exists for group"}

        except Exception as err:
            result = {"result": "failed", "message": "Failed to create filter"}

        return result 


    def delete(self):
        try:
            filter_object = Fuzzy.objects.get(value=self.value).delete()
            result = {"result": "deleted", "message": "Deleted filter from DB"}

        except mongoengine.errors.DoesNotExist:
            result = {"result": "failed", "message": "Filter does not exist"}

        except Exception as err:
            result = {"result": "failed", "message": "Failed to delete filter from DB"}

        return result

