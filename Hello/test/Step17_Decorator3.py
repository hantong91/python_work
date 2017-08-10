#-*- coding: utf-8 -*-
'''


    -decorator 를  class 로 정의하면 더 깔끔하다.
'''
#decorator 역할을 할 class정의하기
class HelloBye:
    # 생성자
    def __init__(self,f):
        #인자로 전달된 함수를 func라는 필드에 저장하기
        self.func=f #원하는시점에 동적으로 필드를 만들수가 있음
        
    #객체를 call 했을때 호출되는 메소드          def wrapper(): 와 같음
    def __call__(self,*args,**kwargs):
        print "hello!"
        self.func(*args,**kwargs)  
        #멤버 메소드 호출하기
        self.sing()
        self.dance()
        print "bye!"  
    
    def sing(self):
        print u"노래를 불러요" 
    def dance(self):
        print u"춤을 춰요"       
@HelloBye
def test1():
    print "test1() called"

if __name__ == '__main__':
    test1()