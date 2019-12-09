from django.db import models

class Inventory(models.Model):
    instanceid = models.CharField(max_length=100)
    instancetype = models.CharField(max_length=100)
    amiid = models.CharField(max_length=100)
    instancestatus = models.CharField(max_length=100)
    az = models.CharField(max_length=100)
    privateip = models.CharField(max_length=100)
    privatednsname = models.CharField(max_length=100)
    publicdnsname = models.CharField(max_length=100)
    publicip = models.CharField(max_length=100)
    keypair = models.CharField(max_length=100)
