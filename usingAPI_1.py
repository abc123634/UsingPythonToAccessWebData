import urllib
import json

# url: http://python-data.dr-chuck.net/comments_166990.json 
url = raw_input("Enter location:")
print("Retrieving {}".format(url))
uh = urllib.urlopen(url)
data = uh.data

print("Retrieving {} characters".format(len(data)))

# print(json.dumps(data, indent=4))
d = json.loads(data)
total = sum(comment['count'] for comment in d['comments'])
print("Sum: {}".format(total))