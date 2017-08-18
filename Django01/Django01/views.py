#-*- coding: utf-8 -*-
'''
Created on 2017. 8. 17.

@author: user
'''
from django.shortcuts import render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect
from _ast import Num
from django.template.context import RequestContext

# 여기는 action클래스 기능을 하는것같음

# root 요청에 대한 응답을 할 메소드
def index(request):
    
    # templates/index.html 페이지를 해석해서 응답하기
    # csrf_token 을 출력하기 위해서는 RequestContext(request) 를 전다해준다.
    return render_to_response("index.html", RequestContext(request)) 

# /hello 용청에 대한 응답을 할 메소드
def hello(request):
    #응답객체를 생성해서
    res=HttpResponse("World!")
    #리턴해준다.
    return res

# /test 요청에 대한 응답을 할 메소드
def test(request):
    '''
        test.html 템플릿을 해석할때 데이터를 dict type 으로 전달한다.
    '''
    return render_to_response("test.html",{"name":u"김구라"}) # test.html을 해석하는데 key가 name인 값을 dict type으로 전달해서 보냄

def show_member(request):
    
    # DB에서 읽어온 회원 정보라고 가정하자
    mem = {"num":1,"name":u"김구라","addr":u"노량진"}
    
    # html 페이지에전달할 dict 에 mem이라는 키값으로 dict type
    # 전달하기
    return render_to_response("show_member.html",{"mem":mem})

def friends(request):
    
    # DB 에서 읽어온 친구 목록이라고 가정하자
    friends=(u"김구라",u"해골",u"원숭이",u"주뎅이",u"덩어리")    
    # dict 에 friends 라는 키값으로 tuple type전달 하기
    return render_to_response("friends.html",{"friends":friends})

def members(request):
    # DB에서 읽어온 회원 목록이라고 가정하자
    mem1={"num":1,"name":u"김구라","addr":u"노량진"}
    mem2={"num":2,"name":u"해골","addr":u"행신동"}
    mem3={"num":3,"name":u"원숭이","addr":u"상도동"}
    
    #회원 목록이 들어잇는 tuple
    members=(mem1,mem2,mem3)
    # dict type이 들어있는  tuple type전달하기
    return render_to_response("members.html", {"members":members})

def detail(request):
    
    #GET 방식 전송 파라미터 추출하기  "/detail?num=999"
    num= request.GET.get("num")
    print "num:", num
    return HttpResponse("detail ok") # 임시응답

def insert(request):
    
    #POST 방식 전송 파라미터 추출하기
    msg = request.POST.get("msg")
    print "msg:" , msg
    return HttpResponse("insert ok")


def gamePlay(request):
    print "/game/play 요청 처리됨!"
    
    # 리다일렉트 이동시키기
    return HttpResponseRedirect("/game/stop/")

def gameStop(request):
    return HttpResponse(u"redirect 이동됨")

# python 에서는 함수를 참조도 가능한데 
# index() 는 호출(call)  a= index 는 참조 이다.





















