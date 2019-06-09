from streaming.app import app
from streaming.config import config
from streaming.transparency.api import Records, Sources, MerkleTree
import faust
import aiohttp

class Tree(faust.Record):
    size: int
    source: str

# Topics
sources_topic = app.topic('ct-sources')
changed_topic = app.topic('ct-sources-changed', value_type=Tree)
cert_decoded_topic = app.topic('ct-certs-decoded')
states_table = app.Table('ct-source-states', default=int)

@app.agent(sources_topic, concurrency=50)
async def get_tree_size(sources):
    base_timeout = aiohttp.ClientTimeout(total=10)
    session = aiohttp.ClientSession(timeout=base_timeout)
    async for source in sources:
        stats =  await Records(source, session).latest()
        if (not source in states_table) or (stats['tree_size'] > states_table[source]):
            await changed_topic.send(value={'source': source, 'size': stats['tree_size']}) 

@app.agent(changed_topic, concurrency=50) 
async def get_records(sources):
    base_timeout = aiohttp.ClientTimeout(total=10)
    session = aiohttp.ClientSession(timeout=base_timeout)
    async for source in sources:
        results = await Records(source.source, session).get(states_table[source.source], source.size)
        if results and 'entries' in results:
            await update_treesize.send(value={'source': source.source, 'size':source.size})
            for certificate in results['entries']:
                await decode_certs.send(value=certificate)

@app.agent(value_type=Tree)
async def update_treesize(sources):
    async for source in sources.group_by(Tree.source):
        states_table[source.source] = source.size

@app.agent()
async def decode_certs(certificates):
    async for certificate in certificates:
        try:
            parsed_cert = MerkleTree(certificate).parse()
            await cert_decoded_topic.send(value=parsed_cert)
        except Exception as err:
            pass


@app.timer(interval=15, on_leader=True)
async def get_sources():
    blacklist = config['transparency']['blacklist']
    sources = await Sources(config['transparency']['base_url']).get()
    print('Pulling latest source file from Google')
    for source in sources['logs']:
        if not source['url'] in blacklist: 
            await sources_topic.send(value=source['url'])
