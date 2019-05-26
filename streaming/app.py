import faust

app = faust.App('faust-transparancy', 
    broker='kafka://localhost:29092',
    origin='streaming',
    autodiscover=['streaming'],
    store='rocksdb://',
    topic_partitions=4,)
