from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # kinda like redirect
from datetime import date

# Create your models here.
class Accs(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('accss_detail', kwargs={'pk': self.id})


class Car(models.Model):
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    link = models.URLField(max_length=300, default="Enter Car URL Here")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accss = models.ManyToManyField(Accs)

    def filled_for_week(self):
        return self.filling_set.filter(date=date.today()).count() >= len(FILLS)


    # this function happens when our create form is submitted,
    # and CarsCreate CBV after it has handled the post request
    def get_absolute_url(self):
        # path('car/int:car_id>/'), views.cars_detail, name='detail'),
        # self.id is referring to the car that was just created when you submit the form
        return reverse('detail', kwargs={'car_id': self.id})
    
    def __str__(self):
        return f"{self.make}"
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for car_id: {self.car_id} @{self.url}"

    

FILLS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)
# select menu ^

# One Car has Many Fillings, a Filling Belongs to a Car
class Filling(models.Model):
    date = models.DateField('Filling Date')
    fill = models.CharField(max_length=1, choices=FILLS, default=FILLS[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_fill_display()} on {self.date}"