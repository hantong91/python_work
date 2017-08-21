#-*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from member import views


urlpatterns = [
   url(r'^list/', views.list),
   url(r'^insertform/', views.insertform),
   url(r'^insert/', views.insert),
   url(r'^delete/', views.delete),
   url(r'^updateform/', views.updateform),
   url(r'^update/', views.update),
]
