import os

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
    }
}