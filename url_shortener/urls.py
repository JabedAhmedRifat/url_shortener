from django.urls import path
from .views import *
urlpatterns = [
    
    
    path('device-list/', allDevicesView),
    path('device-detail/<int:pk>/', devicesDetail),
    path('device-create/', devicesCreate),
    path('device-update/<int:pk>/', devicesUpdate),
    path('device-delete/<int:pk>/', devicesDelete),
    
    
    
    path('urlinfo-list/', allUrlInfoView),
    path('urlinfo-detail/<int:pk>/', urlInfoDetail),
    path('urlinfo-create/', urlInfoCreate),
    path('urlinfo-update/<int:pk>/', urlInfoUpdate),
    path('urlinfo-delete/<int:pk>/', urlInfoDelete),
    
    
    
    path('urlmapping-auth-list/', allUrlMappingLogin),
    path('urlmapping-auth-detail/<int:pk>/', urlMappingLoginDetail),
    path('urlmapping-auth-create/', urlMappingLoginCreate),
    path('a/<str:short_link>/', get_main_link_auth),
    path('urlmapping-auth-update/<int:pk>/', urlMappingLoginCreate),
    path('urlmapping-auth-delete/<int:pk>/', urlMappingLoginDelete),
    
    
    
    path('urlmapping-unauth-list/', allUrlMappingAnno),
    path('urlmapping-unauth-detail/<int:pk>/', UrlMappingAnnoDetail),
    path('urlmapping-unauth-create/', UrlMappingAnnoCreate),
    path('u/<str:short_link>/', get_main_link_unauth),
    path('urlmapping-unauth-update/<int:pk>/', UrlMappingAnnoUpdate),
    path('urlmapping-unauth-delete/<int:pk>/', UrlMappingAnnoUpdate),
    
    
    path('unauth-file-upload/', unauth_upload_csv_and_generate_short_links),
]    