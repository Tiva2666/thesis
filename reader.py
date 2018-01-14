import json
from pprint import pprint
import csv

with open('clean_tweet.txt') as f:
    content = f.readlines()

new_content = []
for line in content:
	new_content.append(json.loads(line))

#test if the file is already cleaned up: 
#for line in new_content:
#	print(line)

#keys = []
#for key in new_content[0]:
#	keys.append(key)

big_container = []
#big_container.append(keys)

print(len(new_content))

for start in range(0, 5):
	container = []
	keys = []
	for key, value in new_content[start].iteritems():
		keys.append(key)
		if (isinstance(value, unicode) or isinstance(value, int)):
			container.append(value)
		else:
			container.append('json_obj')
			#print(type(value))
	big_container.append(keys)			
	big_container.append(container)

# big_container = []
# for start in range(0, len(new_content)):
# 	container = []
# 	for value in new_content[start].iteritems():
# 		print(value)
		#clean_value = value.decode('unicode_escape').encode('ascii','ignore')
		#container.append(clean_value)
	#big_container.append(container)

myFile = open('test.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile)
   writer.writerows(big_container)


#http://stackabuse.com/reading-and-writing-csv-files-in-python/
#