#-*- coding: utf-8 -*-
'''
 Django02_SqliteDB.views.py
'''
from django.shortcuts import render_to_response

def index(request):
    
    return render_to_response("index.html")
