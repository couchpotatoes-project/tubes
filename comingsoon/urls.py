# comingsoon/urls.py
from django.conf.urls import url
from comingsoon import views

urlpatterns = [
    url(r'', views.HomePageView.as_view()),
]