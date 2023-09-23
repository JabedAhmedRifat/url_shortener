from django.db import models
from .base_model import base
from django.contrib.auth.models import User
 
# Create your models here.


class Devices(models.Model):
    mobile = models.BooleanField(default=False)
    desktop = models.BooleanField(default=False)
    other = models.BooleanField(default=False)

class UrlInfo(models.Model):
    ip = models.CharField(max_length=100)
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)


class UrlMappingLogin(base):
    title = models.CharField(max_length=255)
    main_link = models.TextField()
    short_link = models.CharField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(null=True, default=0)
    info = models.ForeignKey(UrlInfo, on_delete=models.CASCADE)
    

class UrlMappingAnno(base):
    main_link = models.TextField()
    short_link = models.CharField(max_length=10)
    
    

    
