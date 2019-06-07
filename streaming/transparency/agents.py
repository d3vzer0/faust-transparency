from streaming.app import app
from streaming.config import config
from streaming.transparency.api import Records, Sources, MerkleTree
import faust

class Tree(faust.Record):
    size: int
    source: str

# Topics
sources_topic = app.topic('ct-sources')
changed_topic = app.topic('ct-sources-changed', value_type=Tree)
update_topic = app.topic('ct-treesize-update', value_type=Tree)
cert_decoded_topic = app.topic('ct-certs-decoded')

# Tables
states_table = app.Table('ct-source-states', default=int)

@app.agent(sources_topic, concurrency=10)
async def get_tree_size(sources):
    async for source in sources:
        try:
            stats = await Records(source).latest()
            result = {'source': source, 'size': stats['tree_size']}
            if (not source in states_table) or (stats['tree_size'] > states_table[source]):
                await changed_topic.send(value=result) 
        except Exception as err:
            pass
    
@app.agent(changed_topic, concurrency=10) 
async def process_sources(sources):
    async for source in sources:
        min_count = states_table[source.source]
        max_count = source.size
        results = await Records(source.source).get(min_count, max_count)
        if results and 'entries' in results:
             # Temporary try/except to debug a log without entries
            try:
                await update_treesize.send(value={'source': source.source, 'size':max_count})
                for certificate in results['entries']:
                    await decode_certs.send(value=certificate)
            except Exception as err:
                pass

@app.agent(update_topic)
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

@app.agent(update_topic)
async def update_treesize(sources):
    async for source in sources.group_by(Tree.source):
        states_table[source.source] = source.size

@app.timer(interval=15)
async def get_sources():
    blacklist = config['transparency']['blacklist']
    sources = await Sources(config['transparency']['base_url']).get()
    print('Pulling latest source file from Google')
    for source in sources['logs']:
        if not source['url'] in blacklist: await sources_topic.send(value=source['url'])