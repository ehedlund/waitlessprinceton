from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import json
import views
import os

from .models import Greeting
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
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

    return render(
      request, 
      'index.html',
      context={'dillonOcc':dillonOcc, 'fristOcc':fristOcc},
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