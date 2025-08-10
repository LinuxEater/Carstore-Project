from django.shortcuts import render
from cars.models import Car
from datetime import datetime
from .models import Team

# Create your views here.

def home(request):
    featured_cars = Car.objects.filter(is_featured=True)
    now = datetime.now()
    teams = Team.objects.all()
    day_of_week = now.strftime('%A') 
    hour = now.strftime('%H:%M')
    context = {
        'teams': teams,
        'day_of_week': day_of_week,
        'featured_cars': featured_cars,
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

