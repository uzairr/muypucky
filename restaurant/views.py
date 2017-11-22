from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from restaurant.models import RestaurantLocation
from restaurant.forms import RestaurantCreateForm


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


def restaurant_create_view(request):
	form = RestaurantCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		obj = RestaurantLocation.objects.create(
			name = form.cleaned_data.get('name'),
			location = form.cleaned_data.get('location'),
			category = form.cleaned_data.get('category'),
			)
		return HttpResponseRedirect('/restaurants/')

	if form.errors:
		errors = form.errors

	template_name = 'restaurant/forms.html'
	context = {
	'form':form,
	'errors': errors
	}
	return render(request, template_name, context)


