#-*- coding: utf-8 -*-

# MyModule.py
nick =u"김구라"

print u"MyModule.py에 실행순서가 들어 왔습니다."

def printNick():
    print "nick:", nick
    
print "MyModule__name__:" , __name__    #__name__ 하면 main으로 나온다 임폴트한게 없으니까