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

class Domain(faust.Record):
    domain: str = ''



class Record(faust.Record):
    firstSeen: str = ''
    resolveType: str = ''
    value: str = ''
    recordHash: str = ''
    lastSeen: str = ''
    resolve: str = ''
    source: list = []
    recordType: str = ''
    collected: str = ''


class PassiveDns(faust.Record):
    totalRecords: int = 0
    firstSeen: str = ''
    lastSeen: str = ''
    results: List[Record] = []

 
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

