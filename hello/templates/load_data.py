import sys,os
import csv
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

dataReader = csv.reader(open(dummy_occupancy.csv), delimiter=',', quotechar='"')
occupancy = []
int index
for row in dataReader:
  occupancy[index] = row[index]
  index+=1
  
