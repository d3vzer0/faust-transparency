from streaming.wordmatching.api.match import Match
from streaming.wordmatching.api.models import Fuzzy, Regex, Whitelist
from streaming.wordmatching.api import Compare
from streaming.app import app
from streaming.config import config
from fuzzywuzzy import fuzz
import csv
import re

# Topics
cert_topic = app.topic('ct-certs-decoded')
update_topic = app.topic('wordmatching-update')
matched_topic = app.topic('wordmatching-hits')
 
# Tables
matching_table = app.Table('matching_table', default=list)
filters = { 'regex': [], 'fuzzy': [], 'whitelist': [] }

@app.task
async def load_fuzzy():
    await update_topic.send(value={'type':'fuzzy'})

@app.task
async def load_regex():
    await update_topic.send(value={'type':'regex'})

@app.task
async def load_whitelist():
    await update_topic.send(value={'type':'whitelist'})

@app.agent(matched_topic)
async def matched_certs(matches):
    async for match in matches:
        print(match)
        url = '{0}://{1}'.format(match['proto'], match['value']).replace('*.', '')
        await Match(url).create('transparency', match['source'], match['input'], match['data'])

@app.agent(cert_topic, concurrency=5)
async def regex_match_ct(certificates):
    async for certificate in certificates:
        if 'CN' in certificate['entry']['subject']:
            domain = certificate['entry']['subject']['CN']
            match_domain = Compare(domain, filters['whitelist']).regex(filters['regex'])
            if match_domain: await matched_topic.send(value={**match_domain, **{'proto':'https', 'data':certificate['entry'] } })

@app.agent(cert_topic, concurrency=5)
async def fuzzy_match_ct(certificates):
    async for certificate in certificates:
        if 'CN' in certificate['entry']['subject']:
            domain = certificate['entry']['subject']['CN']
            match_domain = Compare(domain, filters['whitelist']).fuzzy(filters['fuzzy'])
            if match_domain: await matched_topic.send(value={**match_domain, **{'proto':'https', 'data':certificate['entry'] } })

@app.agent(update_topic)
async def update_filters(matchers):
    print(matchers)
    async for matcher in matchers:
        if matcher['type'] == 'fuzzy':
            filters['fuzzy'] = [{'value':entry['value'], 'likelihood':entry['likelihood']} for entry in Fuzzy.objects()]
        elif matcher['type'] == 'whitelist':
            filters['whitelist'] = [entry['domain'] for entry in Whitelist.objects()]
        elif matcher['type'] == 'regex':
            filters['regex'] = []
            for entry in Regex.objects():
                try:
                    filters['regex'].append(re.compile(entry['value']))
                except Exception as err:
                    print('Invalid regex: {0}'.format(entry['value']))
                    pass
