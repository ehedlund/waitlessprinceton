import sys
import json

# sys.path.append(your_djangoproject_home)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

data = {}
dillonOccupancy = 0
fristOccupancy = 0

with open('current_stats') as f:
	for line in f:
		split = line.split()
		if split[0] == "Dillon-Gym":
			dillonOcc += int(split[2])
		if split[0] == "Frist-Campus-Center":
			fristOcc += int(split[2])
	data['Dillon-Gym'] = dillonOccupancy
	data['Frist-Campus'] = fristOccupancy
	json_data = json.dumps(data)

print 'JSON: ', json_data
