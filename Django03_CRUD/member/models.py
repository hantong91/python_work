#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.fields import AutoField, CharField

# 회원정보를 관리할 모델 설정

# Member 모델 정의
class Member(models.Model):
    # num 필드 설정( 자동 증가 되는 primary key 값)
    num= AutoField(primary_key=True) # 자동증가하는 프라이머리키로 설정  SEQUENSE 만들어서 집어넣은것과 같음
    # name 필드 설정( 최대 길이 : 30, null 허용하지 않음)
    name=CharField(max_length=30,null=False)  
    # addr 필드 설정 ( 최대 길이: 50, null 허용)
    addr=CharField(max_length=50,null=True)
    
    
