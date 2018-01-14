import json
from pprint import pprint
import csv

with open('clean_tweet.txt') as f:
    content = f.readlines()

new_content = []
for line in content:
	new_content.append(json.loads(line))

keys = []
for i in range[0,1000]:
	for key, value in new_content[i].iteritems():
		if key not in keys:
			keys.append(key)

for key in keys:
	print(key)