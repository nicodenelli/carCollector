from django.contrib import admin

# Register your models here.
from .models import Car, Filling

admin.site.register(Car)
admin.site.register(Filling)
