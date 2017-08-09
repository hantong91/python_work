#-*- coding: utf-8 -*-
'''

        -반복문 while
'''

# 제어 변수 0으로 초기화
count1 =0

while count1<10:
    #작업하고
    print count1
    #제어변수값 증가 시키기
    count1 = count1+1

print "-------"

count2=0

while True:
    print count2
    count2+=1
    if count2==9:
        break
       

print u"Step10_while 모듈의 실행순서가 종료 됩니다."   