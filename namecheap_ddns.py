import requests
from config import domains


my_public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']

TEMPLATE_URL = 'https://dynamicdns.park-your-domain.com/update?host=[host]&domain=[domain_name]&password=[ddns_password]&ip=[your_ip]'

for domain in domains:
    for host in domains[domain]['hosts']:
        url = TEMPLATE_URL.replace('[host]', host).replace('[domain_name]', domain).replace(
            '[ddns_password]', domains[domain]['key']).replace('[your_ip]', my_public_ip)
        print('Calling ' + url)
        r = requests.get(url)
        print(str(r))
