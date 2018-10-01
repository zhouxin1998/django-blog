# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# from django.urls import path
from django.conf.urls import url
from .views import index,MySearchView,info,list

# Create your views here.
urlpatterns = [
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^list/(\d+)_(\d+)/$', list),
    url(r'^(\d+)/$', info),
    url(r'^search/', MySearchView()),
]