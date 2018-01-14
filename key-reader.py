import json
from pprint import pprint
import csv

max_range = 1000

with open('clean_tweet.txt') as f:
    content = f.readlines()

new_content = []
for i in range(0, max_range):
	#print(json.loads(content[line]))
	new_content.append(json.loads(content[i]))

keys = [] 
for i in range(0, max_range):
	for key, value in new_content[i].iteritems():
		if key not in keys:
			keys.append(key)

for key in keys:
	print(key)