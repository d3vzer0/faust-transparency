import os

config = {
    'riskiq': {
        'api_key': os.getenv('RISKIQ_KEY', None),
        'username': os.getenv('RISKIQ_USER', None),
        'base_url': os.getenv('RISKIQ_URL', 'https://api.passivetotal.org')
    }
}