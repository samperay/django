from django.shortcuts import render
from django.http import HttpResponse
from inventorymgmt.models import Inventory

def default(request):
    # Displaying default message for project
    return HttpResponse("Welcome to Amazon Inventory Management Systems !")
