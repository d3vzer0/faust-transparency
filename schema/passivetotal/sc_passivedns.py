from typing import List
import faust

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

 