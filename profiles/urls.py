from django.conf.urls import url
from profiles.views import ProfileDetailView

urlpatterns = [
	url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]