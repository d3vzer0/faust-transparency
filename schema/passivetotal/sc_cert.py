from typing import List
import faust

class Cert(faust.Record):
    issuerCountry: str = ''
    subjectCommonName: str = ''
    subjectOrganizationName: str = ''
    subjectOrganizationUnitName: str = ''
    subjectGivenName: str = ''
    subjectSurname: str = ''
    fingerprint: str = ''
    issuerStateOrProvinceName: str = ''
    issuerCommonName: str = ''
    subjectLocalityName: str = ''
    issueDate: str = ''
    subjectEmailAddress: str = ''
    subjectProvince: str = ''
    subjectStateOrProvinceName: str = ''
    issuerEmailAddress: str = ''
    subjectSerialNumber: str = ''
    issuerProvince: str = ''
    issuerOrganizationUnitName: str = ''
    serialNumber: str = ''
    issuerSurname: str = ''
    issuerStreetAddress: str = ''
    issuerLocalityName: str = ''
    subjectStreetAddress: str = ''
    issuerSerialNumber: str = ''
    issuerOrganizationName: str = ''
    sslVersion: str = ''
    sha1: str = ''
    expirationDate: str = ''
    issuerGivenName: str = ''


class SSLSearch(faust.Record):
    queryValue: str
    results: List[Cert]
    success: bool = False
