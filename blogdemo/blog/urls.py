from django.conf.urls import url
from .views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^single/(\d+)/$', single, name='single'),
]


