import faust

class Domain(faust.Record):
    domain: str = ''

