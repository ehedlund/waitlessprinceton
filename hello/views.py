from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import json
import views
#from pyramid.view import view_config

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

@view_config(renderer='json')
def load_json(request):
    return render(request, 'index.html', json_data)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

