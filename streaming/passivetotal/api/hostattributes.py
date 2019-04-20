from streaming.passivetotal.api.riskiq import PassiveTotal

class InvalidField(Exception):
    pass


class HostAtributes(PassiveTotal):
    def __init__(self, search_value):
        self.search_value = search_value
        self.values = ['children', 'parents']
        super(HostAtributes, self).__init__()

    def components(self, **kwargs):
        api_path = '/v2/host-attributes/components'
        query = {'query': self.search_value, **kwargs}
        return self.request(api_path, query)

    def pairs(self, direction, **kwargs):
        if not direction in self.values: raise InvalidField
        api_path = '/v2/host-attributes/pairs'
        query = {'query': self.search_value, 'direction': direction, **kwargs}
        return self.request(api_path, query)

    def trackers(self, **kwargs):
        api_path = '/v2/host-attributes/trackers'
        query = {'query': self.search_value}
        return self.request(api_path, query)

