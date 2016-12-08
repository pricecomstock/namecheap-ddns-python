import requests
from furl import furl

ddnskey= 'YOUR DNS KEY FROM NAMECHEAP'

# This is a dictionary of pairs of domain names and lists of subdomains that should be pointed to the public ip
# {'domain.tld':['sub1','www','blog']}
domains_hosts = {
  '<DOMAIN.TLD>':[
    '<HOST>'
  ]
}

my_public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']

template_url = 'https://dynamicdns.park-your-domain.com/update' # ?host=[host]&domain=[domain_name]&password=[ddns_password]&ip=[your_ip]'

for domain in domains_hosts:
  for host in domains_hosts[domain]:
    f=furl(template_url).set({'host':host,'domain':domain,'password':ddnskey,'ip':my_public_ip})
    print('Calling ' + f.url)
    r=requests.get(f.url)
    print(str(r))
