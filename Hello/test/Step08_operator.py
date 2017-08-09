#-*- coding: utf-8 -*-
"""
    여러가지 연산자 사용해보기 
"""

# 논리연산자 => bool type 데이터를 연산 (and,or,not)

# or 연산 : 연산에 참여하는 bool type 데이터가 어느 하나만
# True 면 결과가 True 이다.
print "-- or 연산 --"
print False or False
print False or True
print True or False
print True or True
# 연산에 참여하는 모든 bool 값이 True 일때 결과는 True 
print "-- and 연산 --"
print False and False
print False and True
print True and False
print True and True
# 논리값을 반전 시킨다. 
print "-- not 연산 --"
print "not True : ", not True
print "not False : ", not False

# 대입연산자 (할당연산자)
name = "kimgura"
num = 10

#num = num+1
num += 1
#num = num+5
num += 5
#num = num-1
num -= 1
#num = num-3
num -= 3
#num = num*2
num *= 2
#num = num/3
num /= 3
#num = num%3 
num %= 3