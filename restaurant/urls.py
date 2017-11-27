from django.conf.urls import url
from restaurant.views import ( 
	RestaurantListView,
	RestaurantDetailView,
	RestaurantUpdateView,
	RestaurantLocationCreateView
	)


urlpatterns = [
    url(r'^create/$', RestaurantLocationCreateView.as_view(), name='create'),
    #url(r'^(?P<slug>[\w-]+)/edit$', RestaurantUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),
    url(r'^(?P<slug>\w+)/$', RestaurantListView.as_view(), name='list'),
    url(r'$', RestaurantListView.as_view(), name='home'),
    ]
