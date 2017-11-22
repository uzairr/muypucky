from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from restaurant.views import ( 
	RestaurantListView,
	RestaurantDetailView,
	RestaurantLocationCreateView
	)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^restaurants/', include('restaurant.urls', namespace='restaurant'), ),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name="contact"),
]
