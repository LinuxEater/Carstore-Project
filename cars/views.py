from django.shortcuts import render
from .models import Car

# Create your views here.

def cars(request):
    all_cars = Car.objects.all()
    context = {
        'all_cars' : all_cars
    }
    return render(request, 'cars/cars.html', context) 
