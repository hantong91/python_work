#-*- coding: utf-8 -*-
'''

    -console 창으로 부터 사용자 입력 받기
    
    raw_input() 빌트인 메소드를 이용해서 문자열 입력 받기
    
'''

msg1 = raw_input(u"메세지 입력:")

print "msg1:",msg1
print "msg1 type:", type(msg1)

msg2 =raw_input(u"메세지 입력(한글포함):")
result = msg2.decode("utf-8")
print "result:", result
print "result type:", type(result)


#문자를 int type 으로 형변환
num1 = int("10")
print num1+1

# 정수 입력 받기
inputNum = int(raw_input(u"숫자 입력:"))
print "inputNum:", inputNum
print "inputNum type:", type(inputNum)



print u"Step01_input 모듈의 실행순서가 종료 됩니다."
