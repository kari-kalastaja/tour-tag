from django.db import models

# Create your models here.
class Destination(models.Model):
    destination = models.CharField(max_length=100)
    arrive_time = models.CharField(max_length=100)
