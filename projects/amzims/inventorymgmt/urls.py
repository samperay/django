from django.conf.urls import include, url
from django.contrib import admin
from inventorymgmt import views
import inventorymgmt

urlpatterns = [
    url(r'^getlist/', inventorymgmt.views.inventory, name='getlist'),
]
