#! /usr/bin/env python
#coding=utf-8
from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','player','result')

admin.site.register(Record,RecordAdmin)    