import requests
import json

payload = {'name': 'Ashish'}
rg = requests.get('https://httpbin.org/get', params=payload)
rp = requests.post('https://httpbin.org/post', data=json.dumps(payload))
ra = requests.get('https://httpbin.org/basic-auth/ashish/testing', auth=('ashish', 'testing'))

print(rg.url)
print(rg.json())
print(rg.status_code)
print('-----------------------------------------------------')
print()

print(rp.url)
print(rp.json())
print(rp.status_code)
print('-----------------------------------------------------')
print()

print(ra.url)
print(ra.text)
print(ra.status_code)
