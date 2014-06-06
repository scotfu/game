#! /usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, url
from .views import push,pull


urlpatterns = patterns('',
    url(r'^record/push/$', push, name='push'),
    url(r'^record/pull/$', pull, name='pull'),
    )
