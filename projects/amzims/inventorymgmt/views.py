from django.shortcuts import render
from django.http import HttpResponse
from inventorymgmt.models import Inventory

def home(request):
    getdetails = Inventory.objects.all()
    #output = ",".join([str(home) for home in getdetails])"
    return HttpResponse(getdetails)

def inventory_detail(request, instanceid):
    return HttpResponse('<p>Instance details with id {} </p>'.format(instanceid))
