from django.shortcuts import render
from django.http import HttpResponse
from inventorymgmt.models import Inventory

def default(request):
    # Displaying default message for project
    return HttpResponse("Welcome to Amazon Inventory Management Systems !")

def inventory(request):
    return HttpResponse("<html> <h1> Amazon Inventory List </h1> </html> ")
