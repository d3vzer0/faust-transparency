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
        domain = certificate['entry_cn']
        for regex in filters['regex']:
            if regex.match(domain) and domain not in filters['whitelist']:
                result = {'source':'regex', 'input':regex.pattern, 
                    'value': domain, 'proto':'https' }
                await matched_topic.send(value=result)
                break

@app.agent(cert_topic, concurrency=5)
async def fuzzy_match_ct(certificates):
    async for certificate in certificates:
        domain = certificate['entry_cn']
        for fuzzy in filters['fuzzy']:
            compare = fuzz.partial_ratio(domain, fuzzy['string'])
            if compare >= int(fuzzy['likelihood']) and domain not in filters['whitelist']:
                result = {'source':'fuzzy', 'input':fuzzy['string'], 
                    'value': domain, 'proto':'https' }
                await matched_topic.send(value=result)
                break

@app.agent(update_topic)
async def update_filters(matchers):
    async for matcher in matchers:

        if matcher['type'] == 'regex':
            filters['regex'] = []
            for entry in matcher['list']:
                filters['regex'].append(re.compile(entry['regex']))
                regex_scoring[entry['regex']] = entry['score']

        elif matcher['type'] == 'fuzzy':
            filters['fuzzy'] = []
            for entry in matcher['list']:
                filters['fuzzy'].append({'string':entry['string'], 'likelihood':entry['likelihood']})
                fuzzy_scoring[entry['string']] = entry['score']

        elif matcher['type'] == 'whitelist':
            filters['whitelist'] = []
            filters['whitelist'] = matcher['list']

@app.task
async def load_fuzzy():
    with open('streaming/wordmatching/config/fuzzy.csv') as fuzzy_file:
        fuzzy_csv = csv.DictReader(fuzzy_file, delimiter=',')
        fuzzy_list = [entry for entry in fuzzy_csv]
        await update_topic.send(value={'type':'fuzzy', 'list':fuzzy_list})

@app.task
async def load_regex():
    with open('streaming/wordmatching/config/regex.csv') as regex_file:
        regex_csv = csv.DictReader(regex_file, delimiter=',')
        regex_list = [entry for entry in regex_csv]
        await update_topic.send(value={'type':'regex', 'list':regex_list})

@app.task
async def load_whitelist():
    with open('streaming/wordmatching/config/whitelist.csv') as whitelist_file:
        whitelist_csv = csv.DictReader(whitelist_file, delimiter=',')
        whitelist = [entry['domain'] for entry in whitelist_csv]
        await update_topic.send(value={'type':'whitelist', 'list':whitelist})





