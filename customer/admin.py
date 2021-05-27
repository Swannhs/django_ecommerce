from django.contrib import admin

# Register your models here.
from customer.models import ShippingAddress, BasicInfo

# admin.site.register(Info)
admin.site.register(ShippingAddress)
admin.site.register(BasicInfo)