import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter url:")

uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
# print(counts)

total = sum(int(count.text) for count in counts)
print(total)
