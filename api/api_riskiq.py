from config import config
import aiohttp

class PassiveTotal:
    def __init__(self):
        self.username = config['riskiq']['username']
        self.api_key = config['riskiq']['api_key']
        self.base_url = config['riskiq']['base_url']

    async def request(self, path, query):
        url = '{0}{1}'.format(self.base_url, path)
        async with aiohttp.ClientSession() as session:
             async with session.post(url, auth=aiohttp.BasicAuth(self.username, self.api_key), json=query) as response:
                 return await response.json()
