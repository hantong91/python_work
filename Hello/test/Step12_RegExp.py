#-*- coding: utf-8 -*-
'''

    정규 표현식 객체 사용하기
    
    -import re 해서 사용한다

'''
import re

#검증할 문자열
myStr = "Hello, World"

result = re.search("Hello", myStr)
result2 = re.search("Hello2", myStr)
print "result:", result
print "result2:", result2

# 참조값이 있는 변수 result VS 없는 변수result2
print "bool(result):", bool(result)
print "bool(result2):",bool(result2)


#검증할 문자열

myStr = "who is who"

#검증할 정규 표현식
reg1="^who"
reg2="^Who"

# 검증 결과를 bool type 으로 받아보기
result4=bool(re.search(reg1,myStr)) #True
result5=bool(re.search(reg2,myStr)) #False

print "result4:",result4
print "result5:",result5




#검증할 문자열
myStr = u"Regular Expression is Powerful! 가나다가나다"

# "r" 이라는 문자열을 모두 찾아서 list type으로 리턴
result5=re.findall(u"r",myStr)

result6=re.findall(u"가",myStr)

print "result5:",result5
print "result6:",result6




#검증할 문자열
myStr = u"$25$ ^^ and $50$"

#정규 표현식에서 특별한 의미를 가지는 문자열을 찾고 싶을때 역슬래시
result7= re.findall(u"\$",myStr)
result8= re.findall(u"\^",myStr)

print result7
print result8


#검증할 문자열

myStr = u"김구라abcd해골^^^^원숭이1234"

result9= re.findall(u"[가-힝]", myStr)
for item in result9:
    print item
    
print "------"    


result9= re.findall(u"[가-힝]+", myStr)
for item in result9:
    print item
    
# 검증할 문자열
myStr = u"abcdefgh0123456789ABCDEFGH!@#!$%가나다라"    

result10 = re.findall(u"[a-zA-Z0-9]", myStr)
result11 = re.findall(u"[\w]",myStr)
for item in result10:
    print item, #한줄로 출력할때
    
print "-------"

for item in result11:
    print item, #한줄로 출력할때    