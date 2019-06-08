import aiohttp
import asyncio

class Records:
    def __init__(self, source, session):
        self.source = source
        self.session = session
 
    async def get(self, min_records, max_records):
        url = 'https://{0}ct/v1/get-entries?start={1}&end={2}'.format(self.source,
            min_records, max_records)
        try:
            async with self.session.get(url) as response:
                return await response.json()
    
        except Exception as err:
            return None

    async def latest(self):
        url = 'https://{0}ct/v1/get-sth'.format(self.source)
        try:
            async with self.session.get(url) as response:
                return await response.json()
    
        except Exception as err:
            return None