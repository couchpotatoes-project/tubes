# comingsoon/urls.py
from django.conf.urls import url
from django.urls import path
from comingsoon import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    path('gamerule/', views.gamerule, name="gamerule")
]