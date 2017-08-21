#-*- coding: utf-8 -*-
'''
Created on 2017. 8. 21.

@author: user
'''
from django.shortcuts import render_to_response

def index(request):
    return render_to_response("index.html")
