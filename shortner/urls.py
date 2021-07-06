from django.urls import path
from .views import home,createUrl, redirect

urlpatterns = [
    path('',home,name='home'),
    path('create/',createUrl,name='create'),
    path('<str:url>',redirect,name='redirect')
    
]