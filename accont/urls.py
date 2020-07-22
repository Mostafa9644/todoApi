from django.urls import path

from .views import rigistration_view

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register',rigistration_view,name='register'),
    path('login',obtain_auth_token,name='login'),

]