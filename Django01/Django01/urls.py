#-*- coding: utf-8 -*-
"""Django01 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from Django01 import views
# 여기가 mvc로 치면 마치 actionfactory 같은 곳인듯
urlpatterns = [
    
    # root (빈) 요청이 들어왔을때 views.py에 있는 index 메소드로
    # 요청 처리하기 ( # ^$ 시작끝사이 아무것도없음 즉 빈 요청에 대해서, views.index 참조)
    url(r"^$",views.index),
    
    # /hello/ 요청이 들어왔을때 views.py 에 있는 hello 메소드로 요청처리하기
    url(r"^hello/$",views.hello),
    
    # /test/ 요청처리
    url(r"^test/$",views.test),
    
    #/show_member/ 요청처리
    url(r"^show_member/$",views.show_member),
    
    #/friends/요청처리
    url(r"^friends/$",views.friends),
    
    #/members/요청처리
    url(r"^members/$", views.members),
    
    #/detail/요청처리
    url(r"^detail/$", views.detail),
    
    #/insert/ post 방식 요청처리
    url(r"^insert/$", views.insert),
    
    #/game/play/ 요청처리
    url(r"^game/play/", views.gamePlay),
    url(r"^game/stop/", views.gameStop),
    
]
