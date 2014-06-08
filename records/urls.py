#! /usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, url
from .views import push,pull,player_status


urlpatterns = patterns('',
    url(r'^record/push/$', push, name='push'),
    url(r'^record/pull/$', pull, name='pull'),
    url(r'^player_status/$', player_status, name='status'),                       
    )
