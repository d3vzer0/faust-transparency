import faust

class Contact(faust.Record):
    organization: str = ''
    email: str = ''
    name: str = ''
    telephone: str = ''


class Whois(faust.Record):
    tech: Contact = {}
    whoisServer: str = ''
    registered: str = ''
    registrar: Contact = {}
    domain: str = ''
    registrant: str = ''
    billing: dict = {}
    telephone: str = ''
    lastLoadedAt: str = ''
    nameServers: list = []
    name: str = ''
    registryUpdatedAt: str = ''
    admin: Contact = {}
    organization: str = ''
    zone: str = ''
    contactEmail: str = ''
    expiresAt: str = ''

