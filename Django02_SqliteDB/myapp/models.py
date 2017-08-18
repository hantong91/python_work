#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

'''
     Data Base 에 테이블을 정의해서 만든다는 느낌으로 클래스를 정의한다.
'''
class Message(models.Model):
    content=models.TextField()
    regdate=models.DateTimeField()