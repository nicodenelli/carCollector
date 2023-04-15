# Create your views here.
from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Add the following import
from django.http import HttpResponse

import uuid
import boto3
from .models import Car, Accs, Photo
from botocore.exceptions import ClientError

from .forms import FillingForm

BUCKET = 'carcollector-sei'
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'


def add_photo(request, car_id):
	# photo-file will be the "name" attribute on the <input name='photo-file' type='file'>
	photo_file = request.FILES.get('photo-file', None)
	if photo_file:
		# setup the aws client 
		s3 = boto3.client('s3')
		# Make a unique name to store the photo			# franklin.png
														# photo_file.name.rfind('.'): this gets us the file exstension .png
			 # store the file in a catcollector folder/randomnumber + the file name with the extension
		key = 'car/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
		try:
			s3.upload_fileobj(photo_file, BUCKET, key)
			# build the url string of where it is hosted to store db
			url = f"{S3_BASE_URL}{BUCKET}/{key}"
			# add it to the db
			Photo.objects.create(url=url, car_id=car_id)
		except ClientError as e:
			print(e, " error from aws!")
		
	return redirect('detail', car_id=car_id)




# the arguments for the commands comes from our urls.py
# 'cars/<int:car_id>/assoc_accs/<int:accs_id>/'
def assoc_accs(request, car_id, accs_id):
	Car.objects.get(id=car_id).accss.add(accs_id)

	# One line version of below^
	# car + Car.objects.get(id=car_id)
	# car.accss.add(accs_id)
	return redirect('detail', car_id=car_id)

# car_id matches the url
# path('cars/<int:car_id>/add_filling/' 
def add_filling(request, car_id):
	# create a modelForm instance using the information from the post request
	# request.POST is like req.body
	form = FillingForm(request.POST)
	# validate the form
	if form.is_valid():
		# don't want to save it until we add the car_id to the feeding
		new_filling = form.save(commit=False)
		# tying the car to the filling
		# defining the FK
		new_filling.car_id = car_id
		new_filling.save()
		# import redirect on the top line from django.shortcuts
	return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
	model = Car
	fields = ['make', 'color', 'model', 'year']
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class CarUpdate(UpdateView):
	model = Car
	# disallow the make as input on the form, so no one can update the make
	fields = ['make', 'color', 'model', 'year', 'link']
	
class CarDelete(DeleteView):
	model = Car
	success_url = '/cars' # <- since we can't redirect to a detail page of a car we deleted



def cars_index(request):
  cars = Car.objects.all() # finding all the cars from the db
  return render(request, 'cars/index.html', {'cars': cars})# <- the blue one

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

def cars_detail(request, car_id):
   car = Car.objects.get(id=car_id)
   # creating a form (instance) from my FillingForm class
   accss_car_doesnt_have = Accs.objects.exclude(id__in = car.accss.all().values_list('id'))

   filling_form = FillingForm()
   return render(request, 'cars/detail.html', {
	   'car': car, 
	   'filling_form': filling_form,
	   'accss': accss_car_doesnt_have
	   })


# Define the home view
# def home(request):
#   return render(request, 'cars/index.html', { 'cars': car })


def about(request):
    # django is configured to know automatically
    # to look inside of a template's folder for the html files
    return render(request, 'about.html')

class AccsList(ListView):
	model = Accs

class AccsDetail(DetailView):
	model = Accs

class AccsCreate(CreateView):
	model = Accs
	fields = '__all__'

class AccsUpdate(UpdateView):
	model = Accs
	fields = ['name', 'color']

class AccsDelete(DeleteView):
	model = Accs
	success_url = '/accss/'
