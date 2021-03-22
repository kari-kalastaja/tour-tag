from django.db import models
from django import forms

# Create your models here.
class Destination(models.Model):
    destination = models.CharField(max_length=100)
    arrive_time = models.CharField(max_length=100)


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

