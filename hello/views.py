from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import sys
import json
import views
import os
import csv
import re
import datetime
from datetime import timedelta
from collections import defaultdict
from .models import Greeting
from django.contrib.auth.decorators import login_required

def roundTime(dt=None, dateDelta=datetime.timedelta(minutes=1)):
    """Round a datetime object to a multiple of a timedelta
    dt : datetime.datetime object, default now.
    dateDelta : timedelta object, we round to a multiple of this, default 1 minute.
    Author: Thierry Husson 2012 - Use it as you want but don't blame me.
            Stijn Nevens 2014 - Changed to use only datetime objects as variables
    """
    roundTo = dateDelta.total_seconds()

    if dt == None : dt = datetime.datetime.now()
    seconds = (dt - dt.min).seconds
    # // is a floor division, not a comment on following line:
    rounding = (seconds+roundTo/2) // roundTo * roundTo
    return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

@login_required
def index(request):
	script_dir = os.path.dirname(__file__)
	rel_path = "static/hello/swipes.csv"
	abs_file_path = os.path.join(script_dir, rel_path)

	traffic = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

	with open(abs_file_path, 'rU') as csvfile:
		spaces = csv.reader(csvfile)
		lineNum = 0
		for line in spaces:
			if lineNum != 0:
				strLine = ','.join(line)
				split = strLine.split(',')
				building = split[0]
				building = re.sub('[-_ ]', '', building)
				time = split[1]
				day = split[2]

				# time processing
				time = split[1].split(':')
				hourInt = int(time[0])
				minute = time[1]
				end = time[2].split()
				if end[1] == "PM" and hourInt != 12:
					hourInt += 12
				elif end[1] == "AM" and hourInt == 12:
					hourInt = 0
# 				hour = str(hourInt)
				second = end[0]
				rounded = roundTime(datetime.datetime(2017,1,4,hourInt,int(minute),int(second)),datetime.timedelta(minutes=30))
				roundedStr = unicode(rounded.replace(microsecond=0))
# 				roundedTime = roundedStr[11:-3]
				formattedTime = "T" + roundedStr[11:-6] + roundedStr[14:-3]

# 				prevTraffic = traffic[building][day][formattedTime]
				traffic[building][day][formattedTime] += 1
			lineNum += 1

	jsonTraffic = json.dumps(traffic)
	jsonTraffic = re.sub('"', '', jsonTraffic);

	return render(
		request, 
		'index.html',
		context={'jsonTraffic':jsonTraffic},
	)

def about(request):
    return render(request, 'about.html')

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
