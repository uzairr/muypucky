from django.conf.urls import url
from menus.views import ( 
	ItemListView,
	ItemDetailView,
	ItemCreateView,
	ItemUpdateView
	)


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/$', ItemListView.as_view(), name='list'),
    url(r'$', ItemListView.as_view(), name='home'),
    ]
