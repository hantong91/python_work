#-*- coding: utf-8 -*-
'''
   - if 문 사용하기
   
   1. 조건부로 특정 블럭을 수행 하고자 할때 사용
   2. 들여쓰기로 특정 블럭을 구성한다.
   
'''
# 단일 if 문

if True :
    print "ok 1"
    print "ok 2"

if False:
    print "ok 3"
    print "ok 4"    

isWait = True

# 조건부 수행

if isWait:
    print "wait!"
    print "wait!"
    print "wait!"
    
# 양자 택일
num=10

if num%2==0:
    print u"{} 은 짝수 입니다.".format(num)
else:
    print u"{} 은 홀수 입니다.".format(num)       




# 다중 if 문
jumsu =85

if jumsu>= 90:
    print u"{} 점은 수 입니다.".format(jumsu)
elif jumsu >=80:
     print u"{} 점은 우 입니다.".format(jumsu)
elif jumsu >=70:
    print u"{} 점은 미 입니다.".format(jumsu)
elif jumsu >=60:
    print u"{} 점은 양 입니다.".format(jumsu)
else:
    print u"{} 점은 가 입니다.".format(jumsu)





# 참고 (3항 연산)

isMan=True

result = u"남자 입니다." if isMan else u"여자 입니다."

"""
 위의 3항 연산의 아래와 같은 로직이다.
result2 = None
if isMan:
    result2=u"남자 입니다."
else:
    result2=u"여자 입니다."
"""

print "isMan : ", result

print u"Step01_if 모듈의 실행 순서가 종료 됩니다."
 

# console 에 띄울때는 상관없지만 db에 들어갈때는 문제가 발생할수 있으므로 한글은 유니코드 타입으로 해야함.









