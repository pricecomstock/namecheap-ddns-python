import requests
from config import domains


IP_API_URL = 'https://api.ipify.org?format=json'
my_public_ip = requests.get(IP_API_URL).json()['ip']

template_url = 'https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain}&password={ddns_key}&ip={ip}'

for domain in domains:
    key = domains[domain]['key']
    for host in domains[domain]['hosts']:

        url = template_url.format(
            host=host, domain=domain, ddns_key=key, ip=my_public_ip)
        print('Calling ' + url)
        r = requests.get(url)
        print(str(r))
