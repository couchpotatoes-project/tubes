"""tubes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include,reverse
from django.conf.urls import include, url
from game import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
    url('^', include('django.contrib.auth.urls')),
	path('gamerule/', views.gamerule, name="gamerule"),
	path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
	#url(r'^admin/', include(admin.site.urls)),
    #path('', include('comingsoon.urls')),
    #path('comingsoon/', include('comingsoon.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	path('home', views.home, name="home"),
	path('tubes', views.tubes, name="tubes"),	
	path('savescore', views.savescore, name='savescore')	
]