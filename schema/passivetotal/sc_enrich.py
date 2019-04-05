import faust

class Enrich(faust.Record):
    subdomains: list = []
    sinkhole: bool = False
    tld: str = ''
    primaryDomain: str = ''
    queryValue: str = ''
    queryType: str = ''
    everCompromised: bool = False
    tag_meta: dict = {}
    classification: str = ''
    tags: list = []
    dynamicDns: str = ''
