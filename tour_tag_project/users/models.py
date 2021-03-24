from django.db import models
from django import forms

# Create your models here.
class Destination(models.Model):
    destination = models.CharField(max_length=100)
    arrive_time = models.CharField(max_length=100)

class Timer(models.Model):
    #savedTime = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    savedTime = models.CharField(max_length=100, blank=True, null=True)
    currentOverTime = models.IntegerField(blank=True, null=True)

class Cities(models.Model):
    city = models.CharField(max_length=100)
    city_can_go1 = models.CharField(max_length=100)
    city_can_go2 = models.CharField(max_length=100, blank=True, null=True)
    city_can_go3 = models.CharField(max_length=100, blank=True, null=True)

class Routes(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrivetime = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)

