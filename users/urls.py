from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

app_name = "users"   


urlpatterns = [
    path("user_details",UserDetailAPIView.as_view()),
    path('register_user',RegisterUserAPIView.as_view()), 
    path('api-auth/', include('rest_framework.urls')),    
]