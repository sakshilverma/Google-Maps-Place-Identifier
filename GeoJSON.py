import urllib.request, urllib.parse, urllib.error
import json

inurl='http://py4e-data.dr-chuck.net/json?'
d=dict()
d['address']=input('Enter location - ')
d['key']=42
url=inurl+urllib.parse.urlencode(d)
print('Receiving url - ',url)
u=urllib.request.urlopen(url).read().decode()
js=json.loads(u)

ans=js['results'][0]['place_id']
print(ans)
