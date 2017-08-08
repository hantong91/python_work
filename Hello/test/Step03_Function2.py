#-*- coding: utf-8 -*-

'''
    파이썬 에서는 함수에 전달받는 인자의 갯수를 
    자유롭게 지정할 수 있다.
    
    *args
       
    -args 는 arguments(인자들)의 약자
    -args 대신에 다른 변수명을 쓸 수도 있지만 관례상 args 라고 한다.
    
    *변수명 을 관례상 *args로 적음
'''

def test(*args): # *args(*인자명) 를 적으면 인자를 안적어도 적어도 인식하기때문에 자유로워진다.
    # args 는 list type 의 read only version 인 tuple type(수정이 불가)
    print "args type:", type(args)
    print args

test()
test(10)
test(10,20)
test(10,20,30)
test("a","b","c")

print "--------"

def test2(a, *args): # 인자에 a가 들어가서 최소1개는 필요함
    print a,args
    
    
 # test2() #오류발생 인자는 최소 1개는 전달해야한다.   
test2(10)    
# "bbb" 는 a 라는 변수에 담기고 10,20,30, 은 tuple로 args에 전달됨
test2("bbb",10,20,30)

print u"Step03_Function2 모듈이 종료 됩니다."     