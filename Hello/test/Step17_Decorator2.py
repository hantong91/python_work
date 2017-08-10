#-*- coding: utf-8 -*-
'''

'''


        # tuple   dict 타입    인자 전달을 타입에 맞게 전달해야 전달됨
def test(*args,**kwargs): # 어떤 인자의 형태도 받아줄수 있는 함수
    print args
    print kwargs
    print "---test()----"
    

# 데코레이터 함수 정의하기
def auth(func):
    def wrapper(*args,**kwargs):
        # decorator 가 적용된 함수에 전달된 인자를 얻어올 수 있다.
        print args,kwargs
        #kwargs 는 dict type 이므로 kwargs["key"] 형태로 참조
        print kwargs["name"], "auth!"
        func(*args,**kwargs)
        print kwargs["name"], "success!"
    return wrapper   

@auth
def updateUser(name):
    print name, u"의 정보를 업데이트 합니다."
@auth
def deleteUser(name):
    print name, u"의 정보를 삭제 합니다."

    
if __name__ == '__main__':
#     test(1)
#     test(1,2)
#     test("a","b","c")
#     test(name="gura")
#     test(isMan=True)
#     test(name="monkey",isMan=False)
#     test("a","b",name="cat",isMan=True)
    updateUser(name="gura")
    deleteUser(name="monkey")