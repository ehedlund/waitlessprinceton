from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import json
import views
import os
#from pyramid.view import view_config

from .models import Greeting

from django.contrib.auth.decorators import login_required
from __main__ import *

# Create your views here.
@login_required
def index(request):
    #occs = {}
    dillonOcc = 0
    fristOcc = 0

    script_dir = os.path.dirname(__file__)
    rel_path = "static/hello/current_stats"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path) as f:
      for line in f:
        split = line.split()
        if split[0] == "Dillon-Gym":
          dillonOcc += int(split[2])
        if split[0] == "Frist-Campus-Center":
          fristOcc += int(split[2])
      #occs['Dillon-Gym'] = dillonOcc
      #occs['Frist-Campus'] = fristOcc

    return render(
      request, 
      'index.html',
      #context={'json_data':json_data},
      context={'dillonOcc':dillonOcc, 'fristOcc':fristOcc},
    )

def about(request):
    return render(request, 'about.html')

def meet(request):
    return render(request, 'meet.html')

def casCGI(request):
    return render(request, 'casCGI.html')

#logout for CAS???
#def logout(request, next_page=None):
 #   """Redirects to CAS logout page"""

  #  from django.contrib.auth import logout
   # logout(request)
   # if not next_page:
   #     next_page = _redirect_url(request)
   # if settings.CAS_LOGOUT_COMPLETELY:
    #    return HttpResponseRedirect(_logout_url(request, next_page))
   # else:
    #    return HttpResponseRedirect(next_page)

def status(request):
    return render(request, 'status.html')

#@view_config(route_name='home', renderer='templates/load_data.py')
#@exception_view_config(ValidationFailure, route_name='home')
#@view_config(renderer='json')
#    return render(request, 'index.html', json_data)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})