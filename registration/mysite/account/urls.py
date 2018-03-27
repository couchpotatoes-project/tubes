from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.success, name='success'),
    path('', views.register, name='register')
    
    ]