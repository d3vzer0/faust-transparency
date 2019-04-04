import faust
from typing import List


class DomainSchema(faust.Record):
    domain: str = ''


class EnrichSchema(faust.Record):
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


class ContactSchema(faust.Record):
    organization: str = ''
    email: str = ''
    name: str = ''
    telephone: str = ''


class WhoisSchema(faust.Record):
    tech: ContactSchema = {}
    whoisServer: str = ''
    registered: str = ''
    registrar: ContactSchema = {}
    domain: str = ''
    registrant: str = ''
    billing: dict = {}
    telephone: str = ''
    lastLoadedAt: str = ''
    nameServers: list = []
    name: str = ''
    registryUpdatedAt: str = ''
    admin: ContactSchema = {}
    organization: str = ''
    zone: str = ''
    contactEmail: str = ''
    expiresAt: str = ''


class RecordSchema(faust.Record):
    firstSeen: str = ''
    resolveType: str = ''
    value: str = ''
    recordHash: str = ''
    lastSeen: str = ''
    resolve: str = ''
    source: list = []
    recordType: str = ''
    collected: str = ''


class PassiveDnsSchema(faust.Record):
    totalRecords: int = 0
    firstSeen: str = ''
    lastSeen: str = ''
    results: List[RecordSchema] = []


class CertSchema(faust.Record):
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


class SSLSearchSchema(faust.Record):
    queryValue: str
    results: List[CertSchema]
    success: bool = False
