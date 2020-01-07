from django.conf.urls import url
from django.contrib import admin
import myapp

urlpatterns = [
    url(r'^hello/', myapp.views.hello, name='hello'),
    url(r'^morning/', myapp.views.morning, name='morning'),
    url(r'^article/(\d+)/', myapp.views.viewArticle, name='article'),
]
