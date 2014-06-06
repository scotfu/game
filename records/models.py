#! /usr/bin/env python
#coding=utf-8
from django.db import models


class Record(models.Model):

    player = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    g_round = models.IntegerField()
    group = models.ForeignKey('Group')
    create_date=models.DateTimeField(auto_now_add=True, verbose_name='finshed time')
    
    def __unicode__(self):
        return self.result

    class Meta:
        verbose_name_plural = "Records"


class Group(models.Model):
    
    name = models.CharField(max_length=100)
    num_of_players = models.IntegerField()
    memo =  models.CharField(max_length=100)
    create_date=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Groups"
        
