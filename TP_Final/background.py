import requests

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.get('https://pub.orcid.org/v2.1/0000-0003-4121-6169/works',headers=headers)
print r.json()