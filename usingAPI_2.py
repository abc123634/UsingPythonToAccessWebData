import urllib 
import json

place = raw_input("Enter location:")

service_url = 'http://python-data.dr-chuck.net/geojson?'
url = service_url + urllib.urlencode({'sensor': 'false', 'address': place})
uh = urllib.urlopen(url)
data = uh.read()

js = json.loads(str(data))
print(json.dumps(js, indent=4))

place_id = js['results'][0]['place_id']
print(place_id)