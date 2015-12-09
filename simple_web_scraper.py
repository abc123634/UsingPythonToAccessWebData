import urllib.request
from bs4 import BeautifulSoup

f = urllib.request.urlopen('http://world.yam.com/')
soup = BeautifulSoup(f.read(), 'lxml')

print(type(soup))

tags = soup('h3')
for tag in tags:
	print (tag)
