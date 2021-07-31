from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

from datetime import date, datetime


class Items(models.Model):
    STATUS = (('Pending', 'Pending'),
    ('Bought', 'Bought'),
    ('Not Available', 'Not Available'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40,null=True,blank=True)
    quantity = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    ordered_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, null=True, blank=True)

    

