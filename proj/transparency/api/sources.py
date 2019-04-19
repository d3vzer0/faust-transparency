import aiohttp
import asyncio

class Sources:
    def __init__(self, base_url='https://www.gstatic.com/ct/log_list/all_logs_list.json'):
        self.base_url = base_url
    
    async def get(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url) as response:
                return await response.json()

