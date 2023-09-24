from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from knox.auth import TokenAuthentication

from .models import *
from .serializers import *
import string
import random
from django.db import IntegrityError


import pandas as pd




# for unauth Upload csv full of url and it become shorten

@api_view(['POST'])
def unauth_upload_csv_and_generate_short_links(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('files')
        if excel_file:
            
            df = pd.read_csv(excel_file)


            url_mappings = []
            for index, row in df.iterrows():
                main_link = row['main_link']

                short_link_length = 8
                short_link = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(short_link_length))

                data = {'main_link': main_link, 'short_link':short_link}
                url_mappings.append(data)
                
            serializer = UrlMappingAnnoSerializer(data=url_mappings, many= True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Data Process successfully', 'url_mappings':serializer.data})
            
            else:
                return Response({'message':'invalid'})
            
            
        else:
            return Response({'message': 'No file uploaded'})
    else:
        return Response({'message': 'Invalid'})


# for Auth Upload Csv and got data 
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def auth_upload_csv_and_generate_short_link(request):
    if request.method == "POST":
        excel_file = request.FILES.get('files')
        if excel_file:
            df = pd.read_csv(excel_file)
            
            
            url_mappings = []
            for index, row in df.iterrows():
                main_link = row['main_link']
                # info_id = request.data.get('info')
                user = request.user
                user_pk = user.pk
                short_link_length = 8
                short_link = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(short_link_length))

                data = {'main_link': main_link, 'short_link':short_link, 'user': user_pk}
                url_mappings.append(data)
            
            serializer = UrlMappingLoginSerializer(data= url_mappings, many=True)
            if serializer.is_valid():
                serializer.save()
                
                serialized_data = [item for item in serializer.data]
                return Response({'messsage':'data Processing successfully', 'url_mappings': serialized_data})
            
            else:
                return Response({'message':'invalid'})
            
            
        else:
            return Response({'message':'no file'})
    else:
        return Response({'message':'invalid'})



# Device Crud

@api_view(['GET'])
def allDevicesView(request):
    if request.method=='GET':
        data = Device.objects.all().order_by('-id')
        serializer = DevicesSerializer(data, many=True)
        return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def devicesDetail(request, pk ):
    data = Device.objects.get(id=pk)
    serializer = DevicesSerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def devicesCreate(request):
    data = request.data 
    serializer = DevicesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def devicesUpdate(request, pk):
    data = Device.objects.get(id = pk)
    serializer = DevicesSerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def devicesDelete(request, pk):
    data = Device.objects.get(id=pk)
    data.delete()
    return Response({
        "message":"Devices deleted successfully"
    })
    
    
    
# Url Info CRUD

@api_view(['GET'])
def allUrlInfoView(request):
    if request.method == "GET":
        data = UrlInfo.objects.all().order_by('-id')
        serializer = UrlInfoSerializer(data, many=True)
        return Response (serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def urlInfoDetail(request, pk):
    data = UrlInfo.objects.get(id=pk)
    serializer = UrlInfoSerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def urlInfoCreate(request):
    data = request.data
    serializer = UrlInfoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def urlInfoUpdate(request,pk):
    data = UrlInfo.objects.get(id=pk)
    serializer = UrlInfoSerializer(instance=data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)





@api_view(['DELETE'])
def urlInfoDelete(request,pk):
    data = UrlInfo.objects.get(id=pk)
    data.delete()
    return Response({'message':'Url Info Deleted Successfully'})






# Url UrlMappingLogin



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def allUrlMappingLogin(request):
    data = UrlMappingLogin.objects.all().order_by('-id')
    serializer = UrlMappingLoginSerializer(data, many=True)
    return Response(serializer.data)






@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def urlMappingLoginDetail(reqeust,pk):
    data = UrlMappingLogin.objects.get(id=pk)
    serializer = UrlMappingLoginSerializer(data)
    return Response(serializer.data)








@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def urlMappingLoginCreate(request):
    if request.method == 'POST':
        main_link= request.data.get('main_link')
        info_id = request.data.get('info')
        if main_link:
            user = request.user
            user_pk = user.pk
            short_link_length = 8
            try:
                short_link = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(short_link_length))
                serializer =  UrlMappingLoginSerializer(data={'main_link':main_link,'short_link':short_link, 'user': user_pk, 'info':info_id, 'count' : 0}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)


            except IntegrityError:
                short_link = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(short_link_length))
                serializer = UrlMappingLoginSerializer(data={'main_link': main_link, 'short_link':short_link, 'user':user_pk, 'info': info_id, 'count' : 0}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
                
                
    
    
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_main_link_auth(request, short_link):
    try:
        url_mapping = UrlMappingLogin.objects.get(short_link=short_link)
        main_link = ({'main_link':url_mapping.main_link})
        
        url_mapping.count += 1
        url_mapping.save()
        
        return Response({'main_link':main_link})
    except UrlMappingLogin.DoesNotExist:
        return Response({'message':'short link doesnot Exist'})

           
    
    
    
    
    



@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def urlMappingLoginDelete(request,pk):
    data = UrlMappingLogin.objects.get(id=pk)
    data.delete()
    return Response({"message":"Url Mapping for logged in user deleted Successfully"})





# Url Mapping Unauthorize User

@api_view(['GET'])
def allUrlMappingAnno(request):
    data = UrlMappingAnno.objects.all().order_by('-id')
    serializer = UrlMappingAnnoSerializer(data, many=True)
    return Response(serializer.data)







@api_view(['GET'])
def UrlMappingAnnoDetail(request, pk):
    data = UrlMappingAnno.objects.get(id=pk)
    serializer = UrlMappingAnnoSerializer(data)
    return Response(serializer.data)








@api_view(['POST'])
def UrlMappingAnnoCreate(request):
    
    data = request.data
    main_link = data.get('main_link')
    if main_link:
            short_link_length = 8
            try:
                short_link = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(short_link_length))
                
                serializer = UrlMappingAnnoSerializer(data={"main_link":main_link,"short_link":short_link},partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.error_messages)
            
            except IntegrityError:
                
                short_link = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(short_link_length))
                serializer = UrlMappingAnnoSerializer(data={'main_link':main_link, "short_link":short_link}, partial=True) 
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
            
                return Response (serializer.errors)          
                    
    else:
            return Response({'error':"invalid"})
        
        
        
        
        
    
@api_view(['GET'])
def get_main_link_unauth(request, short_link):
    try:
        url_mapping = UrlMappingAnno.objects.get(short_link=short_link)
        main_link = url_mapping.main_link
        
        return Response({'main_link': main_link})
    except UrlMappingAnno.DoesNotExist:
        return Response({'error': 'Short link does not exist'})









@api_view(['POST'])
def UrlMappingAnnoUpdate(request,pk):
    data = UrlMappingAnno.objects.get(id=pk)
    serializer= UrlMappingAnnoSerializer(instance=data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)









@api_view(['DELETE'])
def UrlMappingAnnoDelete(request,pk):
    data = UrlMappingAnno.objects.get(id=pk)
    data.delete()
    return Response({"message":"Unauthorize user deleted SuccessFully"})


    
        