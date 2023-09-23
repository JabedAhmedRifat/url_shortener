from rest_framework import serializers
from .models import *

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'
        

class UrlInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlInfo
        fields = '__all__'
        
        
class UrlMappingLoginSerializer(serializers.ModelSerializer):
    class Meta:
        models = UrlMappingLogin
        fields = '__all__'
        

class UrlMappingAnnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlMappingAnno
        fields = "__all__"
    