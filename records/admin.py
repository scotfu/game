#! /usr/bin/env python
#coding=utf-8
from django.contrib import admin
from .models import Record,Group


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','player','result','create_date')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','name','num_of_players','create_date')


    
admin.site.register(Record,RecordAdmin)
admin.site.register(Group,GroupAdmin)    