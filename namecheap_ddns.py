import requests

# This is a dictionary of domain names and details

# If you just need the 'main' host for one domain (if just domain.com was entered):
# DOMAINS = {
#     '<DOMAIN.TLD>': {
#         'hosts':[
#             '@'
#         ],
#         'key':'<YOUR DNS KEY FOR THIS DOMAIN FROM NAMECHEAP>'
#     }
# }

DOMAINS = {
    '<DOMAIN.TLD>': {
        'hosts':[
            '<HOST>',
            '<HOST>'
        ],
        'key':'<YOUR DNS KEY FOR THIS DOMAIN FROM NAMECHEAP>'
    },
    '<DOMAIN2.TLD>': {
        'hosts':[
            '<HOST>',
            '<HOST>'
        ],
        'key':'<YOUR DNS KEY FOR THIS DOMAIN FROM NAMECHEAP>'
    },
}

my_public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']

TEMPLATE_URL = 'https://dynamicdns.park-your-domain.com/update?host=[host]&domain=[domain_name]&password=[ddns_password]&ip=[your_ip]'

for domain in DOMAINS:
    for host in DOMAINS[domain]['hosts']:
        url = TEMPLATE_URL.replace('[host]',host).replace('[domain_name]',domain).replace('[ddns_password]',DOMAINS[domain]['key']).replace('[your_ip]',my_public_ip)
        print('Calling ' + url)
        r=requests.get(url)
        print(str(r))
