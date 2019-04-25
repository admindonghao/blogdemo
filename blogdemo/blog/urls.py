from django.conf.urls import url
from .views import *
from .feed import RssFeed

app_name = 'blog'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^single/(\d+)/$', single, name='single'),
    url(r'^archive/(\d+)/(\d+)/$', archive, name='archive'),
    url(r'^sort/(\d+)/$', sort, name='sort'),
    url(r'^labels/(\d+)/$', labels, name='labels'),
    url(r'^rss/$', RssFeed(), name='rss')
]


