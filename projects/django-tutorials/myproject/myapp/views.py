from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

def hello(request):
   return HttpResponse('Hello World !')

def morning(request):
    return HttpResponse('Morning !')

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)
