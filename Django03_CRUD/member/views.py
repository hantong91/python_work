#-*- coding: utf-8 -*-
from django.shortcuts import render
from member.models import Member
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


    
def list(request):
    # 한 페이지에 몇개의 목록을 출력할지에 대한 값
    PAGE_ROW_COUNT=5
    # 목록 하단에 몇개씩 출력할지에 대한 여부
    PAGE_DISPLAY_COUNT=5
    
    # 번호에 대해 내림 차순 정렬한 전체 목록
    total_list=Member.objects.all().order_by('-num')# >> SELECT * FROM member; 하고 리턴타입을 list로 받음
                                                        # order_by('num') 은 오름차순 order_by('-num') 내림차순
    # 페이징 처리를 도와주는 객체                                                    
    paginator=Paginator(total_list, PAGE_ROW_COUNT)
    # 파라미터로 전달된 페이지 번호
    pageNum=request.GET.get('pageNum')
    
    totalPageCount=paginator.num_pages # 전체 페이지 갯수 
    
    try:
        # 페이지 번호가 넘어온 경우
        member_list=paginator.page(pageNum)
    except PageNotAnInteger:
        # 페이지 번호가 넘어오지 않은 경우
        member_list=paginator.page(1)
        pageNum=1
    except EmptyPage:
        #없는 페이지 번호를 전달한 경우 마지막 페이지를 보여준다.
        member_list=paginator.page(paginator.num_pages)
        pageNum=paginator.num_pages
    # 산술 연산을 하기 위해 숫자로 바꾸기    
    pageNum=int(pageNum)
    
    # 하단 시작 페이지 번호와 끝 페이지 번호 계산하기
    startPageNum=1+((pageNum-1)/PAGE_DISPLAY_COUNT)*PAGE_DISPLAY_COUNT
    endPageNum=startPageNum+PAGE_DISPLAY_COUNT-1
    if totalPageCount < endPageNum:
        endPageNum=totalPageCount
    # 하단 page 번호를 출력할 for 문에 전달하기 위한 range    
    bottomPages=range(startPageNum, endPageNum+1)
    
    return render(
        request,
        'member/list.html', # templates/member/list.html
        {
            'member_list':member_list,
            'pageNum':pageNum,
            'bottomPages':bottomPages,
            'totalPageCount':totalPageCount,
            'startPageNum':startPageNum,
            'endPageNum':endPageNum
        }
    )
    
#     # Member 모델의 모든 데이터를 가지고 온다.
#     member_list=Member.objects.all().order_by('num') 
#     return render(                                                  
#         request,
#         'member/list.html', 
#         {'member_list':member_list},
#     )



#회원 추가 폼 요청 처리
def insertform(request):
    return render(request, 'member/insertform.html')

def insert(request):
    # post 방식 전송 되기 위해서는 form안에 {% csrf_token %} 작성
    # post 방식 전송되는 파라미터 추출해서 Member 모델 객체 생성
    mem = Member(
          name =request.POST.get("name"),
          addr =request.POST.get("addr"),
        )
    # DB에 반영
    mem.save()
    # 리다일렉트 이동하라고 응답
    return HttpResponseRedirect('/member/list/')

def delete(request):
#     # get 방식 전달되는 삭제할 번호 얻어오기
#     num = request.GET.get("num")
#     # 삭제하기
#     mem=Member.objects.get(num=num)
#     mem.delete()
#     
    # 위의 작업을 한줄로 표현하면.....
    Member.objects.get(num=request.GET.get("num")).delete()      #DELETE FROM member WHERE num=? 
    #return HttpResponseRedirect("/member/list/")
    
    return render(
        request,
        'member/alert.html',
        {
            "msg":u"삭제 했습니다.",
            "url":"/member/list"
        },
    )
# 회원정보 수정 form 처리    
def updateform(request):
    # get 방식 전달된 수정할 회원의 번호를 이용해서 회원정보를 얻어온다.
    member=Member.objects.get(num=request.GET.get("num"))
    return render(
        request,
        'member/updateform.html',
        {"member":member},
    )

def update(request):
    member=Member(
        num=request.POST.get("num"),
        name=request.POST.get("name"),
        addr=request.POST.get("addr"),
        )
    #.save()메소드는 data 가있으면 수정 반영, 없으면 insert
    member.save()
    return render(
        request,
        'member/alert.html',
        {"msg":u"수정했습니다.",
         "url":"/member/list/"},
    )
