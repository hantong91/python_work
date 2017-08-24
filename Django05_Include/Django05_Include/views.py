#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import JsonResponse

def index(request):
    return render(request, 'index.html')
def chat(request):
    return render(request,'chat.html')
def game(request):
    return render(request,'game.html')
def includeTest(request):
    return render(request,'includeTest.html')
    
    
    
    
    
    
    
    