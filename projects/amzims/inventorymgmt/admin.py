from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['instanceid', 'instancetype' , 'amiid', 'instancestatus' , 'az', 'privateip', 'privatednsname', 'publicdnsname', 'publicip']
