#! /usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, url
from .views import result


urlpatterns = patterns('',
    url(r'^record/result/$', result, name='result'),
    )
