from app import app, producer
import json


class Streaming:
    def __init__(self, refresh_type):
        self.refresh_type = refresh_type

    async def refresh(self):
        message = json.dumps({'type':self.refresh_type})
        producer.produce(message.encode())