from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomerModel)
admin.site.register(Tag)
admin.site.register(AmbulanceType)
admin.site.register(Booking)

