from django.db import models
from django.urls import reverse # kinda like redirect

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    link = models.URLField(max_length=300, default="Enter Car URL Here")


    # this function happens when our create form is submitted,
    # and CarsCreate CBV after it has handled the post request
    def get_absolute_url(self):
        # path('car/int:car_id>/'), views.cars_detail, name='detail'),
        # self.id is referring to the car that was just created when you submit the form
        return reverse('detail', kwargs={'car_id': self.id})