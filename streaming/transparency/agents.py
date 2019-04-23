from streaming.app import app
from streaming.config import config
from streaming.transparency.api import Records, Sources, MerkleTree

# Topics
sources_topic = app.topic('ct-sources')
changed_topic = app.topic('ct-treesize-changed')
cert_topic = app.topic('ct-certs')

# Tables
states_table = app.Table('ct-source-states', default=int)

@app.agent(sources_topic, concurrency=20)
async def get_tree_size(sources):
    async for source in sources:
        stats = await Records(source).latest()
        result = {'source': source, 'stats': stats}
        if not source in states_table:
            await update_treesize.send(value=result)
        elif stats['tree_size'] > states_table[source]:
            print('Source: {0} - New TreeSize: {1} - Old TreeSize: {2}'.format(source,
                stats['tree_size'], states_table[source]))
            await changed_topic.send(value=result)
    

@app.agent(changed_topic, concurrency=20)
async def process_sources(sources):
    async for source in sources:    
        min_count = states_table[source['source']]
        max_count = source['stats']['tree_size']
        result = await Records(source['source']).get(min_count, max_count)
        await update_treesize.send(value={'source': source['source'], 
            'stats': {'tree_size':max_count}})
        for certificate in result['entries']:
            parsed_cert = MerkleTree(certificate).parse()
            await cert_topic.send(value=parsed_cert)


@app.agent()
async def update_treesize(sources):
    async for source in sources:
        source_url = source['source']
        source_size = source['stats']['tree_size']
        states_table[source_url] = source_size


@app.timer(interval=15)
async def get_sources():
    blacklist = config['transparency']['blacklist']
    sources = await Sources(config['transparency']['base_url']).get()
    print('Pulling latest source file from Google')
    for source in sources['logs']:
        if not source['url'] in blacklist: await sources_topic.send(value=source['url'])



