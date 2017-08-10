#-*- coding: utf-8 -*-
'''
        상속
      
     class 클래스명(상속받을 클래스명)
         pass
'''

class Phone(object):
    #전화 거는 기능
    def call(self):
        print u"전화를 걸어요"
# Phone 클래스를 상속 받아서 클래스 정의하기
class HandPhone(Phone):
    #이동중에 전화를 거는 메소드 
    def mobileCall(self):
        print u"이동중에 전화를 걸어요"
    #사진 찍는 기능
    def takePicture(self):
        print u"100 만 화소의 사진을 찍어요"          
        
class SmartPhone(HandPhone):
    # 인터넷을 하느 ㄴ기능
    def doInternet(self):
        print u"웹서핑을 해요"
    #사진 찍는 기능 재정의
    def takePicture(self):
        print u"1000 만 화소의 사진을 찍어요"         
if __name__ == '__main__':
    #Phone 객체 생성해서 참조값을 phone1이라는 변수에 담기
    phone1 =Phone()
    #HandPhone 객체 생성해서 참조값을 phone2라는 변수에 담기
    phone2 = HandPhone()
    # SmartPhone 객체 생성해서 참조값을 phone3라는 변수에 담기
    phone3 = SmartPhone()
    
    phone1.call()
    print "------"
    phone2.call()
    phone2.mobileCall()
    phone2.takePicture()
    print "------"
    phone3.doInternet()
    phone3.call()
    phone3.mobileCall()
    phone3.takePicture()