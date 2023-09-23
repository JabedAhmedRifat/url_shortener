from rest_framework import serializers
from .models import *

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        

class UrlInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlInfo
        fields = '__all__'
        
        
class UrlMappingLoginSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = UrlMappingLogin
        fields = '__all__'
        

class UrlMappingAnnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlMappingAnno
        fields = "__all__"
    