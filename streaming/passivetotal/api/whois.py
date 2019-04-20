from streaming.passivetotal.api.riskiq import PassiveTotal

class InvalidField(Exception):
    pass


class Whois(PassiveTotal):
    def __init__(self, search_value):
        self.search_value = search_value
        self.values = ['email', 'domain', 'name', 'organization', 'address',
            'phone', 'nameserver' ]
        super(Whois, self).__init__()

    def get(self, **kwargs):
        api_path = '/v2/whois'
        query = {'query': self.search_value, **kwargs}
        return self.request(api_path, query)

    def search(self):
        api_path = '/v2/whois/search/keyword'
        query = {'query': self.search_value}
        return self.request(api_path, query)

    def search_field(self, field):
        if not field in self.values: raise InvalidField
        api_path = '/v2/whois/search'
        query = {'query': self.search_value, 'field': field}
        return self.request(api_path, query)
