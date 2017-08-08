#-*- coding: utf-8 -*- 
# 위에 안적으면 한글이 깨짐

'''
   여러줄 주석입니다.
'''
"""


"""

# 한줄 주석입니다. #으로 시작
# Data Type 확인하기

print 1

print 1+1

print type(1) # int type

print type(10.1) # float type
 
print type(True) # bool type

print type(False)


print type('abcd') #str type
print type("abcd")
print type("한글 ")

print type(u"한글입니다.") #unicod type
print type(u"김구라 abcd")

print type([]) #list type
print type(["aa","bb","cc"])

print type({}) #dict type
print type({"num":1,"name":"gura","isMan":True})

print type({10,20,30}) #set type
print type({"aa","bb","cc"})

print type(None) #NoneType


# myFunction 이라는 이름의 함수 만들기
def myFuntion():
    pass        #pass를 적으면 통과해서 아무것도 일어나지않음
                # 왜 적어놨냐면 아무것도 적지않으면 들여쓰기가 성립하지않아서 오류가남
    print u"하나"
    print u"두울"
    print u"세엣"
    print u"myFunction 이 리턴됩니다."
    
# myFunction 함수 호출하기
myFuntion()    
    
print u"Step01_DataType 모듈로 들어온 실행순서가 종료됩니다." 



               
                