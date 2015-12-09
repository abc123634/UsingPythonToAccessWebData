import urllib.request
from bs4 import BeautifulSoup
import ssl

# f = urllib.request.urlopen('http://world.yam.com/')
# soup = BeautifulSoup(f.read(), 'lxml')

# print(type(soup))

# tags = soup('h3')
# for tag in tags:
# 	print (tag)


"""for coursera homework 1"""
# url = input('Enter - ')
# f = urllib.request.urlopen(url)
# soup = BeautifulSoup(f.read(), 'lxml')

# sum = 0
# count = 0
# spans = soup('span')
# for span in spans:
# 	sum += int(span.contents[0])
# 	count += 1

# print('Count', count)
# print('Sum', sum)

"""for coursera homework 2:"""
url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
print('Retrieving: ', url)

#in case of CERTIFICATE_VERIFY_FAILED
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# uh = urllib.urlopen(url, context=scontext)
f = urllib.request.urlopen(url)
soup = BeautifulSoup(f.read(), 'lxml')

tags = soup('a')
url1 = tags[pos - 1].get('href', None)
print('Retrieving: ', url1)

for i in range(count):
	f1 = urllib.request.urlopen(url1)
	soup1 = BeautifulSoup(f1.read(), 'lxml')
	tags1 = soup1('a')
	print('Retrieving: ', url1)
	url1 = tags1[pos - 1].get('href', None)
