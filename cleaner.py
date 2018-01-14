from os import listdir
from os.path import isfile, join

## read the data from json file folder named twdata
onlyFiles = [f for f in listdir('twdata') if isfile(join('twdata', f))]
newFile = open('clean_tweet.txt','w') 

# for every json file in the folder, do something
for i in range(len(onlyFiles)):
	with open('twdata/' + onlyFiles[i]) as f:
		content = f.readlines()

	# clean up empty lines
	newContent = []
	for line in content:
		if (len(line) > 2): 
			#newContent.append(json.loads(line))
			newFile.write(line)

newFile.close()



