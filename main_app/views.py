from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, make, color, model, year):
    self.make = make
    self.color = color
    self.model = model
    self.year = year

cars = [ # this cars points to below where {'cars': cars}... the blue one
  Car('Camaro', 'racing yellow', 'R/S Zl1', 1969),
  Car('Torino', 'supersonic red', '429 Cobra Jet', 1971),
  Car('Aston Martin', 'Silver Birch', 'DB5', 1964)
]

def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })# <- the blue one

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    # django is configured to know automatically
    # to look inside of a template's folder for the html files
    return render(request, 'about.html')
