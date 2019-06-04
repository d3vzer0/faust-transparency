from streaming.scraper.api.screenshot import Screenshot
from streaming.app import app
from streaming.config import config

# Topics
matched_topic = app.topic('wordmatching-hits')
 
@app.agent(matched_topic, concurrency=5)
async def matched_certs(matches):
    async for match in matches:
        await Screenshot(match['value']).to_png()