from django.shortcuts import render
from datetime import datetime
from .models import Team

# Create your views here.

def home(request):
    now = datetime.now()
    teams = Team.objects.all()
    day_of_week = now.strftime('%A') 
    hour = now.strftime('%H:%M')
    context = {
        'teams': teams,
        'day_of_week': day_of_week,
        'hour': hour,
    }
    return render(request, 'pages/home.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)

