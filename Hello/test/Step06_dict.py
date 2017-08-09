#-*- coding: utf-8 -*-
'''
    -dict type
    
    1. key : value 형태로 데이터를 저장한다.
    2. 순서가 없는 데이터 이다.
    3. key 값을 이용해서 저장된 값을 참조한다.
'''
dict1={"num":1, "name":u"김구라","isMan":True}

# dict type 에 저장된 데이터 참조

print dict1["num"]
print dict1["name"]
print dict1["isMan"]

# 수정
dict["num"]=999 # 대입연산자를 이용해서 특정방의 데이터 수정

#특정방 삭제
del dict1["isMan"]

# 모든방 삭제
dict1.clear()
print u"모든 방 삭제후 dict1:",dict1

dict2={"car":u"자동차", "house":u"집", "phone":u"전화기"}

# dict type 의 key 값 목록
print dict2.keys()

# dict  type 의 value 값만 list type 으로 얻어온다.
print dict2.values()

# for 문에 응용
for key in dict2.keys():
    tmp = dict2[key]
    print key, tmp

