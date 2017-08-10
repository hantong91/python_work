#-*- coding: utf-8 -*-
'''
    
    - decorator 학습하기
'''

def helloBye(func):
    def wrapper():
        print "hello!"
        #helloBye 의 인자로 전달된 함수를 호출
        func()
        print "bye!"       
    return wrapper

# 함수에 helloBye 데코레이터 적용하기
@helloBye
def f1(): # @helloBye 이렇게 함수위에 장식하면 함수의 참조값이 인자로 전달됨
    print u"f1() 함수를 수행했습니다."
@helloBye
def f2():
    print u"f2() 함수를 수행했습니다."
@helloBye    
def f3():
    print u"f3() 함수를 수행했습니다."        

if __name__ == '__main__':
    f1()
    print "------"
    f2()
    print "------"
    f3()
    
    