from proj.app import app
from proj.config import config
from proj.transparency.api import Records, Sources

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
            await changed_topic.send(value=result)


@app.agent(changed_topic, concurrency=20)
async def process_treesize(sources):
    async for source in sources:
        min_count = states_table[source['source']]
        max_count = source['stats']['tree_size'] + min_count
        certs = await Records(source).get(min_count, max_count)
        await process_certs.send(value=certs)

@app.agent()
async def process_certs(certificates):
    async for certificate in certificates:
        cert_topic.send(value=certificate)

@app.agent()
async def update_treesize(sources):
    async for source in sources:
        source_url = source['source']
        source_size = source['stats']['tree_size']
        states_table[source_url] = source_size



@app.timer(interval=10)
async def get_sources():
    blacklist = config['transparency']['blacklist']
    sources = await Sources(config['transparency']['base_url']).get()
    for source in sources['logs']:
        if not source['url'] in blacklist: await sources_topic.send(value=source['url'])



