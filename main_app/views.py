from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

from .models import Car

def cars_index(request):
  cars = Car.objects.all() # finding all the cars from the db
  return render(request, 'cars/index.html', { 'cars': cars })# <- the blue one

# class Car:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, make, color, model, year):
#     self.make = make
#     self.color = color
#     self.model = model
#     self.year = year

# cars = [ # this cars points to below where {'cars': cars}... the blue one
#   Car('Camaro', 'racing yellow', 'R/S Zl1', 1969),
#   Car('Torino', 'supersonic red', '429 Cobra Jet', 1971),
#   Car('Aston Martin', 'Silver Birch', 'DB5', 1964)
# ]



# Define the home view
# def home(request):
#   return render(request, 'cars/index.html', { 'cars': car })
#   return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\</h1>')

def about(request):
    # django is configured to know automatically
    # to look inside of a template's folder for the html files
    return render(request, 'about.html')
