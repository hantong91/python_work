#-*- coding: utf-8 -*-
'''
    
    - 상속받은 부모 클래스의 생성자 호출하는 방법
    
    1. 클래스명.__init__()
    
    2. super(현재 클래스명, self).__init__()
'''
class Car(object):
    #가상의 엔진
    engine=None
    #생성자
    def __init__(self, engine):
        self.engine=engine
    #기능
    def drive(self):
        if self.engine==None:
            print "엔진이 없어서 달릴수가 없어요"
        else:
            print "달려요"

class SuperCar(Car):
    #생성자
    def __init__(self, engine):
        #부모생성자(Car 생성자) 로 필요한 값을 넘겨준다.
        #super(SuperCar, self).__init__(engine) # phthon 2.7 문법
        Car.__init__(self, engine) # 이거나 위에나 같음 아래가 더 기억하기 편하다고함
    
    def driveFast(self):
        if self.engine==None:
            print u"엔진 객체가 없어서 달릴수가 없어요"
        else:
            print u"엄청 빨리 달려요!"
            
if __name__ == '__main__':
    Car(u"엔진").drive()
    Car(None).drive()
    print "---------"
    SuperCar(u"엔진").driveFast()
    SuperCar(None).driveFast()