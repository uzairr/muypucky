from django import forms
from .models import RestaurantLocation

class RestaurantCreateForm(forms.ModelForm):
	class Meta:
		model = RestaurantLocation
		fields = ['name', 'location', 'category', 'slug']

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == "Hello":
			raise forms.ValidationError("Not a valid name")
		return name