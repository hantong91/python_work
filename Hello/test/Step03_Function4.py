#-*- coding: utf-8 -*-


#문자열 format 만들기

result=u"번호:{} 이름:{} 주소:{}".format(1,u"김구라",u"노량진")

#개행을 하려면 엔터칠곳에 \를 붙여서 엔터치면됨
"""
result=u"번호:{} 이름:{} 주소:{}"
\.format(1,u"김구라",u"노량진")

"""
print result
print "-----"


'''

 keyword arguments 를 함수에 전달 받을수도 있다
 
 **kwargs
 
 -kwargs 는 keyward arguments의 약자이다.
 
  딕트 타입으로 (오브젝트) 뭔가 전달할때는 **변수명 을 적으면된다 **변수명은 관례상 *kwargs로 한다.
  '''

def test(**kwargs):
    print "kwargs type:", type(kwargs)
    print kwargs
    
test()
test(num=1)
test(num=1,name=u"김구라",isMan=True)
test(num=1,awef=2,aefaw="wefaef")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    