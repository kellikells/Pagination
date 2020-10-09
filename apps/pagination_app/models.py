from __future__ import unicode_literals
from django.db import models
from django import forms
# for regular expressions 
import re 
# for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class Lead(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    # page_num = models.IntegerField()
    # page_num = models.CharField(max_length= 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return('first_name= ' + self.first_name)