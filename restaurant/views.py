from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from restaurant.models import RestaurantLocation
from restaurant.forms import RestaurantCreateForm


class RestaurantListView(LoginRequiredMixin, ListView):
	def get_queryset(self, *args, **kwargs):
		return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self, *args, **kwargs):
		return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantLocationCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantCreateForm
	template_name = 'forms.html'
	#success_url = '/restaurants/'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestaurantLocationCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantLocationCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = "Add Restaurant"
		return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantCreateForm
	login_url = '/login/'
	template_name = 'restaurant/detail-update.html'

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().name
		context['title'] = "Update Restaurant: {}".format(name)
		return context

	def get_queryset(self, *args, **kwargs):
		return RestaurantLocation.objects.filter(owner=self.request.user)
