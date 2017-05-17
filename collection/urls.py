from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import *  # NOQA
from collection.views import WineListView, WineDetailView


app_name = 'collection'
urlpatterns = [
	url(r'^$', WineListView.as_view(), name='collection-list'),
	url(r'^(?P<slug>[-\w]+)/$', WineDetailView.as_view(), name='collection-details'),
]