from django.conf.urls import url
from restaurant.views import ( 
	RestaurantListView,
	RestaurantDetailView,
	RestaurantLocationCreateView
	)


urlpatterns = [
    url(r'^create/$', RestaurantLocationCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>\w+)/$', RestaurantListView.as_view(), name='list'),
    url(r'$', RestaurantListView.as_view(), name='home'),
    ]
