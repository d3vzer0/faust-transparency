from app.models import Matches
import mongoengine

class Match:
    def __init__(self, url):
        self.url = url

    def create(self, datasouce):
        try:
            target_object = Matches(url=self.url, datasource=datasource).save()
            result = {"result": "success", "message":"Added target to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result": "failed", "message": "Target already exists"}

        except Exception as e:
            result = {"result": "failed", "data": "Failed to create target"}

        return result