#-*- coding: utf-8 -*-

# str type 데이터를 만들어서 참조 값을 변수에 담기
myComment = "abcdeee"

print "id:", id(myComment) #아이디값 확인
print u"길이:", len(myComment) #문자열의 길이 확인
print u"e 의 포함 횟수:", myComment.count("e")
print u"시작하는 글자 확인:", myComment.startswith("a") 

# + 가 아니고 , 로 문자열을 연결

name1=u"김구라"
name2=u"이정호"
name3=u"김구라"

print "name1 id:", id(name1)
print "name2 id:", id(name2)
print "name3 id:", id(name3)

# name1 과 name3은 내용이 같고 참고값까지도 같음 즉 내용이 같으면 참조값도 일치함
# java에서는 담기는 내용이 같다고 해서 참조값까지도 같지는않았음 새로 생성한 객체마다 참조값이 다르기때문

isEqual= name1==name2
isEqual2 = name1==name3

print "name1 == name2 :", isEqual
print "name1 == name3 :", isEqual2 
