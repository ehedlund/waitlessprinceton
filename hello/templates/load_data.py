import sys
import json

# sys.path.append(your_djangoproject_home)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

data = {}
dillonOcc = 0
fristOcc = 0

with open('current_stats') as f:
	for line in f:
		split = line.split()
		if split[0] == "Dillon-Gym":
			dillonOcc += int(split[2])
		if split[0] == "Frist-Campus-Center":
			fristOcc += int(split[2])
	data['Dillon-Gym'] = dillonOcc
	data['Frist-Campus'] = fristOcc
	json_data = json.dumps(data)
