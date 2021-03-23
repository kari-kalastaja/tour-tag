from django.contrib import admin
from .models import Destination, Cities, Routes
# Register your models here.

admin.site.register(Destination)
admin.site.register(Cities)
admin.site.register(Routes)