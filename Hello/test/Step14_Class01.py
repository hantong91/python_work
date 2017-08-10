# -*- coding: utf-8 -*-
'''
    -객체를 생성하기 위한 설계도 : class 정의하기

'''
# Car 클래스 정의하기

class Car:                                   # public class Car(){
    #필드(속성,저장소)                                    public String name 소나타;          
    name=u"소나타"
    
    #메소드(기능,함수)                                    public void drive(){
    def drive(self):                                    # System.out.println("달려요")
        print u"달려요"                                    #}
                                                        #}
    #메소드
    def showInfo(self):
        # self 에는 객체의 참조값이 전달된다.
        print u"차의 이름:", self.name
            
if __name__ == '__main__':
    # Car 클래스를 이용해서 객체를 생성하고 참조값을 변수에 담기
    car1=Car()
    # Car 객체의 필드 참조해서 콘솔에 출력하기
    print "car1.name:", car1.name
    #Car 객체의 메소드 호출하기
    car1.drive()
    car1.showInfo()
    #type 출력해보기
    print "car1 type:",type(car1)