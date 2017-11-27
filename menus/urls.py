from django.conf.urls import url
from menus.views import ( 
	ItemListView,
	ItemDetailView,
	ItemCreateView,
	ItemUpdateView
	)


urlpatterns = [
	#url(r'^(?P<pk>\d+)/edit$', ItemUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'$', ItemListView.as_view(), name='home'),
    ]
