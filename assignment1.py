import re

f = open('regex_sum_166984.txt', 'r')
content = f.read()

matches = re.findall('[0-9]+', content)
sum = 0
for match in matches:
	sum += int(match)

print(sum)