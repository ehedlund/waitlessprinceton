from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Building, BuildingInstance

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

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
