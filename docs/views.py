from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def statussite(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
