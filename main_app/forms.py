from django.forms import ModelForm
from .models import Filling 

class FillingForm(ModelForm):
	class Meta:
		model = Filling 
		fields = ['date', 'fill']