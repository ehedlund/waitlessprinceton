from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from pyramid.view import view_config

from .models import Greeting

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def meet(request):
    return render(request, 'meet.html')

def casCGI(request):
    return render(request, 'casCGI.html')

def status(request):
    return render(request, 'status.html')

@view_config(renderer='json')
def (request):
    return json_data

def load(request):
    return JsonResponse

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

