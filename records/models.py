#! /usr/bin/env python
#coding=utf-8
from django.db import models

class Record(models.Model):

    player = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.result

    class Meta:
        verbose_name_plural = "Records"
