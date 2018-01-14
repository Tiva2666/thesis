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
	'twitter_filter_level',
	'retweetCount',
	'info',
	'location',
	'inReplyTo'
]

headers = [
	'id',
	'objectType',
	'actor.id',
	'actor.displayName',
	'actor.followersCount',
	'verb',
	'postedTime',
	'generator.link',
	'generator.displayName',
	'provider.link',
	'provider.displayName',
	'provider.objectType',
	'link',
	'body',
	'object.postedTime',
	'favoritesCount',
	'twitter_filter_level',
	'retweetCount',
	'info',
	'location',
	'inReplyTo'
]


keys_object = []

max_range = 3000

with open('clean_tweet.txt') as f:
    content = f.readlines()

new_content = []
for i in range(0, max_range):
	#print(json.loads(content[line]))
	new_content.append(json.loads(content[i]))

big_container = []
big_container.append(headers)
for content in new_content:
	container = []
	for ky in used_keys:
		try:
			if (isinstance(content[ky], unicode) or isinstance(content[ky], int)):
				if (ky == 'body'):
					container.append(content[ky].encode('utf-8'))
				elif (ky == 'id'):
					idstr = content[ky].split(':')
					container.append(idstr[2])
				else:
					container.append(content[ky])
			else:
				if (ky == 'actor'):
					idstr = content[ky]['id'].split(':')
					container.append(idstr[2])
					container.append(content[ky]['displayName'].encode('utf-8'))
					container.append(content[ky]['followersCount'])
				elif (ky == 'object'):
					container.append(content[ky]['postedTime'])
				elif (ky == 'generator'):
					container.append(content[ky]['link'])
					container.append(content[ky]['displayName'].encode('utf-8'))
				elif (ky == 'provider'):
					container.append(content[ky]['link'])
					container.append(content[ky]['displayName'].encode('utf-8'))
					container.append(content[ky]['objectType'])
				elif (ky == 'twitter_entities'):
					print(content[ky]['hashtags'])
					container.append(content[ky]['user_mentions'].encode('utf-8'))
				else: 
					container.append('object')
				# print (ky)
				# for key in content[ky].keys():
				# 	print ('-- ' + key)
		except Exception as e:
			container.append('-')
	big_container.append(container)

  
with open(str(max_range) + '.csv', 'w') as myFile:  
	writer = csv.writer(myFile)
	writer.writerows(big_container)
		
