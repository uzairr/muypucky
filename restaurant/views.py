from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from restaurant.models import RestaurantLocation

class RestaurantListView(ListView):
	model = RestaurantLocation
	def get_queryset(self, *args, **kwargs):
		slug = self.kwargs.get('slug')
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug)|Q(category__icontains=slug)
				)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	# def get_object(self, *args, **kwargs):
	# 	slug = self.kwargs.get('slug')
	# 	obj = get_object_or_404(RestaurantLocation, pk=slug)
	# 	return obj