from streaming.config import config
import faust

app = faust.App('faust-transparancy', 
    broker=config['stream']['host'],
    autodiscover=[config['stream']['app']],
    store='rocksdb://',
    topic_partitions=4,
    stream_wait_empty=False)
