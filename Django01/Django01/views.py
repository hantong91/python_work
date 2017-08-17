#-*- coding: utf-8 -*-
'''
Created on 2017. 8. 17.

@author: user
'''
from django.shortcuts import render_to_response
from django.http.response import HttpResponse

# root 요청에 대한 응답을 할 메소드
def index(request):
    
    # templates/index.html 페이지를 해석해서 응답하기
    return render_to_response("index.html")

# /hello 용청에 대한 응답을 할 메소드
def hello(request):
    #응답객체를 생성해서
    res=HttpResponse("World!")
    #리턴해준다.
    return res