#-*- coding: utf-8 -*-
import re
import os
import codecs

sample=u"a  b  c  ddd         eeee"

result=re.split(r"[\t ]+",sample) 

print result




cwd=os.getcwd()
filePath=cwd+os.sep+"testFile.txt"
f=codecs.open(filePath,"r","utf-8")

while True:
    data=f.readline()
    if data=="":
        break #반복문 블럭 빠져 나오기
    print data
    
#위의 예제를 참고해서 검색어를 입력받아서
inputKeyword=raw_input("검색할 동,면,리 입력:")
decodedKeyword=inputKeyword.decode("utf-8")
 
#해당 검색어에 관련된 모든 주소를 출력해 보세요.


#파일 열기
zipPath=os.getcwd()+os.sep+"zipcode.txt"
zipFile=codecs.open(zipPath,"r","utf-8")

print u"검색중..."

while True:
    #한줄씩 읽어온다.
    data=zipFile.readline()
    if data=="":
        break
    # 한줄의 정보를 list type 으로 받아온다.
    info=re.split(r"[\t ]+",data) # tap 혹은 공백이 하나 이상인 글자로 구분하겠다
    
    #배열의 3번째 방에 입력한 키워드가 존재하는지 여부
    result = bool(re.search(decodedKeyword, info[3]))
    if result:
        print data
        
zipFile.close() # 파일 닫기


#파일 열기
zipFile = codecs.open(zipPath,"r","utf-8")

# 동을 입력하면 우편번호를 출력해 보세요
inputKeyword=raw_input("우편번호를 알고 싶은 동 입력:")
decodedKeyword=inputKeyword.decode("utf-8")

print u"검색중..."
while True:
    #한줄씩 읽어온다.
    data=zipFile.readline()
    if data=="":
        break
    # 한줄의 정보를 list type 으로 받아온다.
    info=re.split(r"[\t ]+",data) # tap 혹은 공백이 하나 이상인 글자로 구분하겠다
    
    #배열의 3번째 방에 입력한 키워드가 존재하는지 여부
    result = bool(re.search(decodedKeyword, info[0])) # info의 인덱스: 0번 우편번호 1번 시 2번 구 3번 동 4번 건물 5번 건물번호
    if result:
        print data
        
zipFile.close() # 파일 닫기

