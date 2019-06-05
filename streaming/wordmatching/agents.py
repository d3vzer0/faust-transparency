from streaming.wordmatching.api.match import Match
from streaming.wordmatching.api.models import Fuzzy, Regex, Whitelist
from streaming.app import app
from streaming.config import config
from fuzzywuzzy import fuzz
import csv
import re

# Topics
cert_topic = app.topic('ct-certs')
update_topic = app.topic('wordmatching-update')
matched_topic = app.topic('wordmatching-hits')
 
# Tables
matching_table = app.Table('matching_table', default=list)
regex_scoring = app.Table('regex_scoring', default=int)
fuzzy_scoring = app.Table('fuzzy_scoring')

filters = {
    'regex': [],
    'fuzzy': [],
    'whitelist': []
}

@app.agent(cert_topic, concurrency=5)
async def regex_match_ct(certificates):
    async for certificate in certificates:
        if 'CN' in certificate['entry']['subject']:
            domain = certificate['entry']['subject']['CN']
            for regex in filters['regex']:
                if regex.match(domain) and domain not in filters['whitelist']:
                    result = {'source':'regex', 'input':regex.pattern, 
                        'value': domain, 'proto':'https' }
                    await matched_topic.send(value=result)
                    break

@app.agent(cert_topic, concurrency=5)
async def fuzzy_match_ct(certificates):
    async for certificate in certificates:
        if 'CN' in certificate['entry']['subject']:
            domain = certificate['entry']['subject']['CN']
            for fuzzy in filters['fuzzy']:
                compare = fuzz.partial_ratio(domain, fuzzy['value'])
                if compare >= int(fuzzy['likelihood']) and domain not in filters['whitelist']:
                    result = {'source':'fuzzy', 'input':fuzzy['value'], 
                        'value': domain, 'proto':'https' }
                    await matched_topic.send(value=result)
                    break

@app.agent(update_topic)
async def update_filters(matchers):
    async for matcher in matchers:
        if matcher['type'] == 'fuzzy':
            filters['fuzzy'] = []
            fuzzy_filters = Fuzzy.objects()
            for entry in fuzzy_filters:
                filters['fuzzy'].append({'value':entry['value'], 'likelihood':entry['likelihood']})
                fuzzy_scoring[entry['value']] = entry['score']

        elif matcher['type'] == 'whitelist':
            filters['whitelist'] = []
            whitelist = Whitelist.objects()
            for entry in whitelist:
                filters['whitelist'].append(entry['domain'])

        elif matcher['type'] == 'regex':
            filters['regex'] = []
            regex_filters = Regex.objects()
            for entry in regex_filters:
                try:
                    filters['regex'].append(re.compile(entry['value']))
                    regex_scoring[entry['value']] = entry['score']
                except Exception as err:
                    print('Invalid regex: {0}'.format(entry['value']))
                    pass

@app.agent(matched_topic)
async def matched_certs(matches):
    async for match in matches:
        print(match['value'], match['source'], match['input'])
        await Match(match['value']).create('transparency', match['source'], match['input'])


@app.task
async def load_fuzzy():
    await update_topic.send(value={'type':'fuzzy'})

@app.task
async def load_regex():
    await update_topic.send(value={'type':'regex'})

@app.task
async def load_whitelist():
    await update_topic.send(value={'type':'whitelist'})

