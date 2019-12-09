from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p> Home View </p>')

def inventory_detail(requestm, instanceid):
    return HttpResponse('<p>Instance details with id {} </p>'.format(instanceid))
