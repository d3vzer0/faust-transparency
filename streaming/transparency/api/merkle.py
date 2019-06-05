from streaming.transparency.api import ctl
from OpenSSL import crypto 
import base64


class Certificate:
    def __init__(self, certificate):
        self.certificate = certificate

    def details(self):
        issuer = self.certificate.get_issuer()
        subject = self.certificate.get_subject()
        decoded_certificate = {
            'issuer': {component[0].decode('utf-8'):component[1].decode('utf-8') \
                for component in issuer.get_components()},
            'not_after': self.certificate.get_notAfter().decode('utf-8'),
            'not_before': self.certificate.get_notBefore().decode('utf-8'),
            'serial': str(self.certificate.get_serial_number()),
            'algorithm': self.certificate.get_signature_algorithm().decode('utf-8'),
            'version': self.certificate.get_version(),
            'subject': {component[0].decode('utf-8'):component[1].decode('utf-8') \
                for component in subject.get_components()},
            'fingerprint': self.certificate.digest("sha1").decode('utf-8') }

        return  decoded_certificate


class MerkleTree(Certificate):
    def __init__(self, entry):
        leaf_input = base64.b64decode(entry['leaf_input'])
        self.leaf_data = ctl.MerkleTreeHeader.parse(leaf_input)
        self.extra_data = base64.b64decode(entry['extra_data'])

    def precert(self):
        data_object = ctl.PreCertEntry.parse(self.extra_data)
        entry = Certificate(crypto.load_certificate(crypto.FILETYPE_ASN1, data_object.LeafCert.CertData)).details()
        chain = [Certificate(crypto.load_certificate(crypto.FILETYPE_ASN1, cert.CertData)).details() \
            for cert in data_object.Chain]
        result = {'type':'precert', 'entry':entry, 'chain':chain}
        return result
       
    def log(self):
        extra_data = ctl.CertificateChain.parse(self.extra_data)
        entry = Certificate(crypto.load_certificate(crypto.FILETYPE_ASN1, ctl.Certificate.parse(self.leaf_data.Entry).CertData)).details()
        chain = [Certificate(crypto.load_certificate(crypto.FILETYPE_ASN1, cert.CertData)).details() \
            for cert in extra_data.Chain]
        result = {'type':'log', 'entry':entry, 'chain':chain}
        return result

    def parse(self):
        parse_functions = { 'X509LogEntryType': self.log,
            'PrecertLogEntryType': self.precert }
        decode_tree = parse_functions[self.leaf_data.LogEntryType]()
        return decode_tree
     