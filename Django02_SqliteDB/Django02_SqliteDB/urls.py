#-*- coding: utf-8 -*-
"""Django02_SqliteDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Django02_SqliteDB import views

urlpatterns = [
    # superuser 요청에 대한 응답 
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    # myapp.urls.py 를 포함 시키기
    url(r'^message/', include('myapp.urls')),
]













