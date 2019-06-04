from streaming.scraper.api.models import Snapshots
import hashlib
import mongoengine

class Snapshot:
    def __init__(self, url):
        self.url = url

    async def create(self, data):
        try:
            sha256 = hashlib.sha256(data).hexdigest()
            snapshot_output = Snapshots(url=self.url,sha256=sha256)
            snapshot_output.screenshot.put(data, content_type="image/png")
            snapshot_output.save()
            result = {"result": "success", "data": "Succesfully inserted snapshot result"}

        except Exception as err:
            result = {"result": "failed", "data": "Failed to insert snapshot"}

        return result
