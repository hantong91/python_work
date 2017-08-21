#-*- coding: utf-8 -*-
from django.contrib import admin
from member.models import Member

# Register your models here.

# 관리자 모드에서 관리할 모델 정보 설정
class MemberAdmin(admin.ModelAdmin):
    #num, name, addr 필드를 볼 수 있도록 설정
    list_display=('num','name','addr')
    
# 등록하기
admin.site.register(Member, MemberAdmin)    