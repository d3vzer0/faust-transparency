from streaming.passivetotal.api import PassiveTotal
from streaming.app import app
import streaming.passivetotal.models as Schema


source_topic = app.topic('input-enrich-domains', value_type=Schema.Domain)
result_table = app.Table('output-enrich-domains', default=dict)

# Produce whois records
@app.agent(app.topic('output-domains-whois'))
async def output_whois(results):
    async for result in results:
        result_table[result['domain']]['whois'] = result['response']
        yield result

# Lookup whois records
@app.agent(source_topic, concurrency=10)
async def lookup_whois(domains):
    async for domain in domains:
        response = await PassiveTotal.Whois(domain.domain).get()
        result = {'domain': domain, 'response': response}
        await output_whois.send(value=result)    

# Produce enrichment records
@app.agent(app.topic('output-domains-enrichment'))
async def output_enrichment(results):
    async for result in results:
        result_table[result['domain']]['enrichment'] = result['response']
        yield result

# Lookup enrichment records
@app.agent(source_topic, concurrency=10)
async def lookup_enrichment(domains):
    async for domain in domains:
        response = await PassiveTotal.Enrichment(domain.domain).get()
        result = {'domain': domain, 'response': response}
        await output_enrichment.send(value=result)

# Produce passivedns records
@app.agent(app.topic('output-domains-passivedns'))
async def output_passivedns(results):
    async for result in results:
        result_table[result['domain']]['passivedns'] = result['response']
        yield result

# Lookup passivedns records
@app.agent(source_topic, concurrency=10)
async def lookup_passivedns(domains):
    async for domain in domains:
        response = await PassiveTotal.PassiveDNS(domain.domain).get()
        result = {'domain': domain, 'response': response}
        await output_passivedns.send(value=result)

# Produce ssl records
@app.agent(app.topic('output-domains-ssl'))
async def output_ssl(results):
    async for result in results:
        result_table[result['domain']]['ssl'] = result['response']
        yield result

# Lookup ssl records
@app.agent(source_topic, concurrency=10)
async def lookup_ssl(domains):
    async for domain in domains:
        response = await SSL(domain.domain).get()
        result = {'domain': domain, 'response': response}
        await output_ssl.send(value=result)

