#-*- coding: utf-8 -*-

'''
    가상의 Coffee 객체를 생성할수 있는 클래스 정의
    가상의 Starbucks 객체를 생성할수 있는 클래스 정의
'''

class Coffee:
    #커피를 먹는 메소드
    def eat(self):
        print u"얌얌"

class StarBucks:
    #필드
    branch=None #지점명을 저장할 메소드
    def __init__(self,branch):
        #인자로 전달된 지점명을 필드에 저장하는 code작성
        self.branch=branch
    def showBranch(self):
        #필드에 저장된 필드명을 콘솔에 출력하는 code 작성
        print self.branch
    def getCoffee(self):
        # Coffee 객체를 생성해서 참조값을 리턴해주는 code작성
        return Coffee()
    def getCoffees(self,amount):
        #인자로 전달되는 int type만큼 Coffee객체를 생성해서
        #list type 에 담아서 리턴해주는 code 작성
        Coffees=[]
        for i in range(amount):
            Coffees.append(Coffee())
        return Coffees
        
if __name__ == '__main__':
    star1=StarBucks(u"구로지점")
    star2=StarBucks(u"종로지점")
    
    star1.showBranch()
    star2.showBranch()
    
    print"----------"
    
    #Coffee 객체 리턴 받아서 eat()메소드 호출
    star1.getCoffee().eat()
    #StarBucks 구로지점에서 Coffee 객체 5개를list type 으로 받기
    myCoffee = star1.getCoffees(5)
    print "-------------"
    
    #list type 에 들어있는 모든 Coffee 객체의 메소드
    # 순서대로 호출하기
    for item in myCoffee:
        item.eat()
        
    print u"__main__ 의 실행순서가 종료됩니다."    