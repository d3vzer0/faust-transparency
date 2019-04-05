from config import config
import aiohttp

class Threatstream:
    def __init__(self):
        self.username = config['threatstream']['username']
        self.api_key = config['threatstream']['api_key']
        self.base_url = config['threatstream']['base_url']

    async def request(self, query):
        url = '{0}/intelligence/?username={1}&api_key={2}&status=active{3}'.format(self.base_url,
            self.username, self.api_key, query)
        async with aiohttp.ClientSession() as session:
             async with session.get(url) as response:
                 return await response.json()
