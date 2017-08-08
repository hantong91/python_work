#-*- coding: utf-8 -*-

# 함수에 전달받는 인자의 default 값을 지정할 수도 있다.

def test(num=0):
    print "num:", num
    
test()
test(999)

def test2(num=0, name=u"아무개", isMan=True):
    print "num:",num    
    print "name:",name
    print "isMan:",isMan

test2()
print "-------"
test2(1,u"김구라")
print "-------"
test2(2,u"해골",False)
 
    
