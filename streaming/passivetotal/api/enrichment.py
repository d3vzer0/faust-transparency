from streaming.passivetotal.api.riskiq import PassiveTotal

class Enrichment(PassiveTotal):
    def __init__(self, search_value):
        self.search_value = search_value    
        super(Enrichment, self).__init__()
    
    def get(self):
        api_path = '/v2/enrichment'
        query = {'query': self.search_value}
        return self.request(api_path, query)

    def malware(self):
        api_path = '/v2/enrichment/malware'
        query = {'query': self.search_value}
        return self.request(api_path, query)

    def osint(self):
        api_path = '/v2/enrichment/osint'
        query = {'query': self.search_value}
        return self.request(api_path, query)

    def subdomains(self):
        api_path = '/v2/enrichment/subdomains'
        query = {'query': self.search_value}
        return self.request(api_path, query)
