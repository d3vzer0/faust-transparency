from api import PassiveDNS, Enrichment, Whois, SSL
import faust

app = faust.App('riskiq-enricher', broker='kafka://localhost')
class DomainSchema(faust.Record):
    domain: str

source_topic = app.topic('input-domains', value_type=DomainSchema)

# Produce whois records
@app.agent(app.topic('output-domains-whois'))
async def output_whois(domains):
    async for domain in domains:
        yield domain

# Lookup whois records
@app.agent(source_topic, concurrency=10)
async def lookup_whois(domains):
    async for domain in domains:
        response = await Whois(domain.domain).get()
        await output_whois.send(value=response)

# Produce enrichment records
@app.agent(app.topic('output-domains-enrichment'))
async def output_enrichment(domains):
    async for domain in domains:
        yield domain

# Lookup enrichment records
@app.agent(source_topic, concurrency=10)
async def lookup_enrichment(domains):
    async for domain in domains:
        response = Enrichment(domain.domain).get()
        await output_enrichment.send(value=response)

# Produce passivedns records
@app.agent(app.topic('output-domains-passivedns'))
async def output_passivedns(domains):
    async for domain in domains:
        yield domain

# Lookup passivedns records
@app.agent(source_topic, concurrency=10)
async def lookup_passivedns(domains):
    async for domain in domains:
        response = PassiveDNS(domain.domain).get()
        await output_passivedns.send(value=response)
    
# Produce ssl records
@app.agent(app.topic('output-domains-ssl'))
async def output_ssl(domains):
    async for domain in domains:
        yield domain

# Lookup ssl records
@app.agent(source_topic, concurrency=10)
async def lookup_ssl(domains):
    async for domain in domains:
        response = SSL(domain.domain).get()
        await output_ssl.send(value=response)
