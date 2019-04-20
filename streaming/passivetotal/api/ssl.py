from streaming.passivetotal.api.riskiq import PassiveTotal

class InvalidField(Exception):
    pass


class SSL(PassiveTotal):
    def __init__(self, search_value):
        self.search_value = search_value
        self.values = ['issuerSurname', 'subjectOrganizationName', 'issuerCountry',
            'issuerOrganizationUnitName', 'fingerprint', 'subjectOrganizationUnitName',
            'serialNumber', 'subjectEmailAddress', 'subjectCountry', 'issuerGivenName',
            'subjectCommonName', 'issuerCommonName', 'issuerStateOrProvinceName',
            'issuerProvince', 'subjectStateOrProvinceName', 'sha1', 'subjectStreetAddress',
            'subjectSerialNumber', 'issuerOrganizationName', 'subjectSurname', 'subjectLocalityName',
            'issuerStreetAddress', 'issuerLocalityName', 'subjectGivenName', 'subjectProvince',
            'issuerSerialNumber', 'issuerEmailAddress']
        super(SSL, self).__init__()

    def search(self):    
        api_path = '/v2/ssl-certificate/search/keyword'
        query = {'query': self.search_value}
        return self.request(api_path, query)

    def search_field(self, field):
        if not field in self.values: raise InvalidField
        api_path = '/v2/ssl-certificate/search'
        query = {'query': self.search_value, 'field': field}
        return self.request(api_path, query)

    def history(self):
        api_path = '/v2/ssl-certificate/history'
        query = {'query': self.search_value}
        return self.request(api_path, query)

    def get(self):
        api_path = '/v2/ssl-certificate'
        query = {'query': self.search_value}
        return self.request(api_path, query)

    