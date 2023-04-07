from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, year, make, model, color):
    self.year = year
    self.make = make
    self.model = model
    self.color = color

cars = [ # this cars points to below where {'cars': cars}... the blue one
  Car(1969, 'Camaro', 'R/S Zl1', 'racing yellow'),
  Car(1971, 'Torino', '429 Cobra Jet', 'supersonic red'),
  Car(1964, 'Aston Martin', 'DB5', 'Silver Birch')
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
