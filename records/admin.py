#! /usr/bin/env python
#coding=utf-8
from django.contrib import admin
from .models import Record,Group,Parameter


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','player','result','g_round','create_date')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','name','num_of_players','create_date')

class ParameterAdmin(admin.ModelAdmin):
    list_display = ('id','name','value')
    

    
admin.site.register(Record,RecordAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Parameter,ParameterAdmin)    