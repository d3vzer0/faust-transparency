import os
import yaml

config = {
    'riskiq': {
        'api_key': os.getenv('RISKIQ_KEY', None),
        'username': os.getenv('RISKIQ_USER', None),
        'base_url': os.getenv('RISKIQ_URL', 'https://api.passivetotal.org')
    },
    'threatstream': {
        'api_key':  os.getenv('THREATSTREAM_KEY', None),
        'username': os.getenv('THREATSTREAM_USER', None),   
        'base_url': 'https://api.threatstream.com/api/v2'
    },
    'transparency': {
        'base_url': 'https://www.gstatic.com/ct/log_list/all_logs_list.json',
        'blacklist': yaml.safe_load(open('streaming/transparency.yml'))['transparency']['blacklist']
    },
    'selenium': {
        'host': os.getenv('GRID_HOST', 'localhost:4444'),
        'browser': os.getenv('GRID_BROWSER', 'chrome')
    },
    'stream': {
        'app': os.getenv('STREAM_NAME', 'streaming.transparency'),
        'host': os.getenv('KAFKA_HOST', 'kafka://localhost:29092')
    }
}