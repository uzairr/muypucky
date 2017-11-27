from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from restaurant.views import ( 
	RestaurantListView,
	RestaurantDetailView,
	RestaurantLocationCreateView
	)
from profiles.views import ProfileFollowToggle


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^restaurants/', include('restaurant.urls', namespace='restaurant'), ),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^u/', include('profiles.urls', namespace='profiles'), ),
    url(r'^items/', include('menus.urls', namespace='menus'), ),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name="contact"),
]
