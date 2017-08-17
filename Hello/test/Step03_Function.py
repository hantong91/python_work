#-*- coding: utf-8 -*-

#test1 이라는 이름의 빈 함수 만들기

def test1():
    pass
#test2 라는 이름의 함수 만들기
def test2():
    print u"test2 함수가 호출됨"
    
test1()
test2()    

#함수의 인자를 1개 전달 받는 함수

def test3(a):
    print u"전달받은 내용:",a
    
test3(u"김구라")
test3(999)   
test3() # 전달안하면 오류가 난다.

#함수의 인자를 2개 전달받는 함수
def test4(arg1,arg2):
    print "arg1:",arg1
    print "arg2:",arg2
    

test4(u"하나",u"두울")        

# None 을 리턴하는 3개의 함수
def test5():
    print "test5()"
def test6():    
    print "test6()"
    return
def test7():
    print "test7()"
    return None

# javascript :undefine+null 을 합친것과 비슷함/ java : null
# return을 안적거나 return만 적거나 return None 하면 None타입이 리턴됨

# unicode type 을 리턴하는 함수
def test8():
    print "test8()"
    return u"김구라"


result1 = test5()
result2 = test6()
result3 = test7()
result4 = test8()

print "result1:", result1
print "result2:", result2
print "result3:", result3
print "result4:", result4


print u"step03_Function 모듈의 실행 순서가 종료됩니다."