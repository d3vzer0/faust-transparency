from streaming.config import config
import aiohttp

class PassiveTotal:
    def __init__(self, username, api_key, base_url='https://api.passivetotal.org'):
        self.username = username
        self.api_key = api_key
        self.base_url = base_url

    async def request(self, path, query):
        url = '{0}{1}'.format(self.base_url, path)
        async with aiohttp.ClientSession() as session:
             async with session.post(url, auth=aiohttp.BasicAuth(self.username, self.api_key), json=query) as response:
                 return await response.json()
