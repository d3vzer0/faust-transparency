from api.threatstream import Threatstream

class InvalidField(Exception):
    pass


class Entities(Threatstream):
    def __init__(self, search_type):
        self.search_type = search_type
        self.values = ['ip', 'domain', 'url', 'md5', 'email']
        super(PassiveDNS, self).__init__()

    def get(self, search_value):
        if not self.search_type in self.values: raise InvalidField
        api_path = '&itype={}&value={}'.format(self.search_type, search_value)
        return self.request(api_path)
        
      