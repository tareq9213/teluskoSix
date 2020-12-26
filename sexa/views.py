from django.shortcuts import render, HttpResponse
from .models import Destinations

def home(request):

    dests = Destinations.objects.all()
    return render(request, 'index.html', {'dests': dests})
