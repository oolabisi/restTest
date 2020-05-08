"""games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include

# app_name = 'gamesApp'

urlpatterns = [
    url(r'^', include('drones.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),

    #   url(r'^v1/', include('drones.urls', namespace= 'v1')),
    #   url(r'^v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^v2/', include('drones.v2.urls', namespace= 'v2')),
    # url(r'^v2/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #  url(r'^', include('gamesApp.urls')),
    # path('admin/', admin.site.urls),

    url(r'^', include('drones.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
