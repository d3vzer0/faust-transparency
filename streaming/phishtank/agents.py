from streaming.app import app
from streaming.config import config
from streaming.phishtank.api import Reported

# Topics
reports_topic = app.topic('phishtank-reports')

# Tables
states_table = app.Table('phishtank-state', default=str)

@app.agent(reports_topic)
async def get_phishtank_reports(states):
    async for state in states:
        try:
            phishtank_reports = await Reported('API_KEY').get(states_table['size'], state['size'])
            for report in phishtank_reports:
                print(report)
                # Do things
            await update_etag.send(state)

        except Exception as err:
            print(err)
            pass

@app.agent()
async def update_etag(states):
    async for state in states:
        states_table['etag'] = state['etag']
        states_table['size'] = state['size']
        

@app.task
async def hallo():
    phishtank_state = await Reported('API_KEY').latest()
    if not states_table['etag'] or states_table['etag'] != phishtank_state['etag']:
        await get_phishtank_reports.send(value=phishtank_state)
