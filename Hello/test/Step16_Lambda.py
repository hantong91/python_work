#-*- coding: utf-8 -*-
'''
    - lambda 함수 익히기
'''

def printHi():
    print "hi hi hi"
    
def useFunction(f):
    # 전달된 인자를 함수로 간주하고 함수 호출하기
    f()
    print u"useFunction() 함수가 리턴 합니다."    

#인자로 전달받은 두수의 합을 리턴해주는 함수
    
def getSum(x,y):
    return x+y
    
if __name__ == '__main__':
    #main 으로 실행했을때 실행순서가 들어오는곳
    
    #python 에서는 함수도 객체이므로 변수에 담을수 있다.
    
    #함수 호출
    printHi()
    #함수를 참조해서 변수에 대입
    a= printHi
    #변수에 대입된 함수의 참조값을 이용해서 함수 호출 가능
    a()
    
    print "-------"
    #함수를 호출하면서 함수의 참조값 전달하기
    useFunction(a)
    
    result = getSum(10,10)
    print "result :",result
    
    print "lambda 함수 정의해서 사용하기"
    '''
    
    (lambda x, y: x+y)(10,10)
        는 javascript 에서 
    (function(x,y){return x+y})(10,10);
    
        와 같다
    '''
    
    print "lambda 함수 사용 결과:",(lambda x,y:x+y)(10,10) 
    
    
    # lambda 함수 만들어서 참조값 변수에 담기
    myLam= lambda x,y: x*y
    
    print "myLam(10,10):" ,myLam(10,10)
    