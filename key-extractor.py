import json
from pprint import pprint
import csv

used_keys = [
	'id',
	'objectType',
	'actor',
	'verb',
	'postedTime',
	'generator',
	'provider',
	'link',
	'body',
	'object',
	'favoritesCount',
	'twitter_entities',
	'twitter_filter_level',
	'retweetCount',
	'info',
	'location',
	'inReplyTo'
]

keys_object = []

max_range = 1

with open('clean_tweet.txt') as f:
    content = f.readlines()

new_content = []
for i in range(0, max_range):
	#print(json.loads(content[line]))
	new_content.append(json.loads(content[i]))

big_container = []
big_container.append(used_keys)
for content in new_content:
	container = []
	for ky in used_keys:
		try:
			if (isinstance(content[ky], unicode) or isinstance(content[ky], int)):
				if (ky == 'body'):
					container.append(content[ky].encode('utf-8'))
				else:
					container.append(content[ky])
			else:
				container.append('object')
				print (ky)
				for key in content[ky].keys():
					print ('-- ' + key)
		except Exception as e:
			container.append('-')
	big_container.append(container)

  
with open(str(max_range) + '.csv', 'w') as myFile:  
	writer = csv.writer(myFile)
	writer.writerows(big_container)
		
