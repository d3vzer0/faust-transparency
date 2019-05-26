from app.models import Regex
import mongoengine

class Regex:
    def __init__(self, value):
        self.value = value

    def create(self, score):
        try:
            filter = Regex(value=self.value, score=score).save()
            result = {"result": "created", "message": "Succesfully created filter"}

        except mongoengine.errors.NotUniqueError:
            result = {"result": "failed", "message": "Filter already exists for group"}

        except Exception as err:
            result = {"result": "failed", "message": "Failed to create filter"}

        return result
    
    def delete(self):
        try:
            filter_object = Regex.objects.get(value=self.value).delete()
            result = {"result": "deleted", "message": "Deleted filter from DB"}


        except mongoengine.errors.DoesNotExist:
            result = {"result": "failed", "message": "Filter does not exist"}

        except Exception as err:
            result = {"result": "failed", "message": "Failed to delete filter from DB"}

        return result

