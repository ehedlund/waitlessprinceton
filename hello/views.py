from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import sys
import json
import views
import os
import csv
import datetime
from datetime import timedelta
from django import template
register = template.Library()

from .models import Greeting
from django.contrib.auth.decorators import login_required

# @login_required
# def index(request):
#     dillonOcc = 0
#     fristOcc = 0

#     script_dir = os.path.dirname(__file__)
#     rel_path = "static/hello/current_stats"
#     abs_file_path = os.path.join(script_dir, rel_path)

#     with open(abs_file_path) as f:
#       for line in f:
#         split = line.split()
#         if split[0] == "Dillon-Gym":
#           dillonOcc += int(split[2])
#         if split[0] == "Frist-Campus-Center":
#           fristOcc += int(split[2])

#     return render(
#       request, 
#       'index.html',
#       context={'dillonOcc':dillonOcc, 'fristOcc':fristOcc},
#     )

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

@register.tag('getIndex', getIndex)
def getIndex(List, i):
    return List[int(i)]

@login_required
def index(request):
	
	dillonOcc = 0
	dctBuild = {'ATRIUMCAFE':0, 'BUTLERCOLLEGE':1, 'CAFEVIVIAN':2, 'CENTERFORJEWISHLIFE':3, 'CHANCELLORGREEN':4, 
			'CHEMISTRYCAFE':5, 'CONCESSIONS_12':6, 'FORBESCOLLEGE':7, 'FRISTCSTORE':8, 'FRISTGALLERY1':9, 
			'FRISTGALLERY2':10, 'FRISTGALLERY3':11, 'FRISTGALLERY4':12, 'FRISTWITHERSPOONS':13, 'GRADUATECOLLEGE':14,
			'LIBRARY_CART':15, 'MATHEYCOLLEGE':16, 'ROCKEFELLERCOLLEGE':17, 'STUDIO34BUTLEREMPORIUM':18, 
			 'WHITMANCOLLEGE':19, 'WILSONCOLLEGE':20, 'WOODROWWILSONCAFE':21, "FIRESTONELIBRARY":22}
	dctDay = {'MONDAY':0, 'TUESDAY':1, 'WEDNESDAY':2, 'THURSDAY':3, 'FRIDAY':4, 
			'SATURDAY':5, 'SUNDAY':6}
	dctTime = {	'T0000':0, 'T0030':1, 'T0100':2, 'T0130':3, 'T0200':4, 
			'T0230':5, 'T0300':6, 'T0330':7, 'T0400':8, 'T0430':9, 
			'T0500':10, 'T0530':11, 'T0600':12, 'T0630':13, 'T0700':14,
			'T0730':15, 'T0800':16, 'T0830':17, 'T0900':18, 'T0930':19, 
			'T1000':20, 'T1030':21, 'T1100':22, 'T1130':23, 'T1200':24, 
			'T1230':25, 'T1300':26, 'T1330':27, 'T1400':28, 'T1430':29, 
			'T1500':30, 'T1530':31, 'T1600':32, 'T1630':33, 'T1700':34,
			'T1730':35, 'T1800':36, 'T1830':37, 'T1900':38, 'T1930':39, 
			'T2000':40, 'T2030':41, 'T2100':42, 'T2130':43, 'T2200':44, 
			'T2230':45, 'T2300':46, 'T2330':47}

	script_dir = os.path.dirname(__file__)
	rel_path = "static/hello/current_stats"
	abs_file_path = os.path.join(script_dir, rel_path)

	script_dir = os.path.dirname(__file__)
	rel_path = "static/hello/swipes.csv"
	abs_file_path = os.path.join(script_dir, rel_path)
	swipeData = [[[0 for k in xrange(48)] for j in xrange(7)] for i in xrange(23)]

	with open(abs_file_path) as f:
		for line in f:
			split = line.split()
			if split[0] == "Dillon-Gym":
			  dillonOcc += int(split[2])

	with open(abs_file_path, 'rU') as csvfile:
		spaces = csv.reader(csvfile)
		lineNum = 0
		for line in spaces:
			if lineNum != 0:
				strLine = ','.join(line)
				#strLine = strLine[:-3]
				#print strLine
				split = strLine.split(',')
				building = ''.join(split[0].split())
				building = building.upper()
				if split[0] == "Frist C-Store":
					building = building[:6] + building[7:]
				day = split[2].upper()
				time = split[1].split(':')
				hourInt = int(time[0])
				minute = time[1]
				end = time[2].split()
				if end[1] == "PM" and hourInt != 12:
					hourInt += 12
				elif hourInt == 12:
					hourInt = 0
				hour = str(hourInt)
				second = end[0]
				rounded = roundTime(datetime.datetime(2017,1,4,int(hour),int(minute),int(second)),datetime.timedelta(minutes=30))
				roundedStr = unicode(rounded.replace(microsecond=0))
				roundedTime = roundedStr[11:-3]
				#print "rounded time" + roundedTime
				formattedTime = "T" + roundedTime[:2] + roundedTime[3:]
				swipeData[dctBuild[building]][dctDay[day]][dctTime[formattedTime]] += 1
			lineNum += 1

	return render(
	request, 
	'index.html',
	context={'swipeData':swipeData, 'dillonOcc':dillonOcc},
	)

def about(request):
    return render(request, 'about.html')

def status(request):
    return render(request, 'status.html')

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
