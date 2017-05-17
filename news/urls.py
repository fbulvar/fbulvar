from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import *  # NOQA
from news.views import NewsListView, NewsDetailView


app_name = 'news'
urlpatterns = [
	url(r'^$', NewsListView.as_view(), name='news-list'),
	url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news-details'),
]