from streaming.passivetotal.api.riskiq import PassiveTotal

class PassiveDNS(PassiveTotal):
    def __init__(self, search_value):
        self.search_value = search_value
        super(PassiveDNS, self).__init__()

    def search(self):
        api_path = '/v2/dns/search/keyword'
        query = {'query': self.search_value}
        return self.request(api_path, query)

    def get(self, **kwargs):
        api_path = '/v2/dns/passive'
        query = {'query': self.search_value, **kwargs}
        return self.request(api_path, query)

    def unique(self, **kwargs):
        api_path = '/v2/dns/passive/unique'
        query = {'query': self.search_value, **kwargs}
        return self.request(api_path, query)
