import aiohttp
import asyncio


class Reported:
    def __init__(self, api_key):
        self.timeout = aiohttp.ClientTimeout(total=10)
        self.api_key = api_key
        self.url = 'http://data.phishtank.com/data/{0}/online-valid.json'.format(self.api_key)

    async def request(self, session, url):
        async with session.get(url) as response:
            return await response.json()

    async def state(self, session, url):
        async with session.head(url, allow_redirects=True) as response:
            result = {'etag':response.headers['Etag'], 'size':response.headers['Content-Length']}
            return result
        
    async def get(self, min_bytes, max_bytes):
        try:
            headers = {'Range': 'bytes={0}-{1}'.format(int(min_bytes), int(max_bytes))}
            async with aiohttp.ClientSession(timeout=self.timeout, headers=headers) as session:
                return await self.request(session, self.url)
    
        except Exception as err:
            print(err)
            return None

    async def latest(self):
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                return await self.state(session, self.url)

        except Exception as err:
            print(err)
            return None