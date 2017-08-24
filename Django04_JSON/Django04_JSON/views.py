#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import JsonResponse

def index(request):
    return render(request, 'index.html')

def json01(request):
    # json 응답할 데이터 
    mem={'num':1, 'name':u'김구라', 'isMan':True}
    # dict type 을 json 문자열로 응답하기 
    return JsonResponse(mem)

def json02(request):
    # json 응답할 데이터
    nums=[10, 20, 30, 40, 50]
    # list type 을 json 문자열로 응답하기
    return JsonResponse(nums, safe=False) # array 형태를 출력하기 위해
    
def json03(request):
    # post 방식 전송된 파라미터 추출 
    msg = request.POST.get("msg")
    print "msg:", msg
    # json 문자열 응답 
    return JsonResponse({'result':'success'}) 
    
    
    
    
    
    
    
    
    
    