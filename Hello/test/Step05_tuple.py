#-*- coding: utf-8 -*-
'''
    - tuple
    
    1. list type 과 유사
    2. 읽기 전용(저장된 데이터 수정, 삭제 불가)
    3. list 에 비해 속도가 빠르다
'''


tuple1=("one","two","three")

print tuple1[0] # list type 과 참조하는 방식이 같다

a= tuple1[2] #2번방 참조해서 다른 변수에 담기

print a
# 수정 불가(read only)
#tuple1[1] ="test"  : TypeError: 'tuple' object does not support item assignment

#tuple type 을 list type으로 변환해서 새로운 객체 얻어내기
list1=list(tuple1) #list class 의 생성자를 호출하는것
print "list1:",list1

# list type 을 tuple type 으로 변환해서 새로운 객체 얻어내기
tuple2 = tuple(list1) #tuple class의 생성자 호출
print "tuple2:", tuple2

#tuple1 관 tuple2 의 참조값 비교

result = tuple1==tuple2  # 내용비교   .equals()
print "tuple1==tuple2:", result

result2 = tuple1 is tuple2 # 정확한 참조값 비교   ==
print "tuple1== tuple2:", result2

num1=10
num2=10

print "num1==num2:", num1==num2
print "num1 is num2:",num1 is num2 # 파이썬은 모두 객체 타입이다. 숫자의 경우 숫자가같으면 객체참조값도 같아서 is도 성립

#방 1개 짜리 tuple 객체 만들때는 주의!

nums= [10]

# 일반 괄호와 구분하기 위해서 우측에 , 를 하나 붙여준다.  그냥 적으면 괄호속에들어있는 숫자로 인식해서 타입이 int로 나온다.
# 따라서 연산에서는 ,를 사용하지 않기때문에 ,를 적으면 tuple로 인식되는것
nums2=(10)

print type(num2)

nums3=10,20,30  #굳이 괄호를 사용하지 않아도 tuple을 만들수 있다.

print "nums3:", nums3
print type(nums3)

# 3개의 변수에 동시에 값 대입하기
num1, num2, num3= 1,2,3
print num1,num2,num3
myFriends =("gura","monkey","dog")
#tuple 에 있는 값을각각의 변수에 대입하기
a,b,c = myFriends
print a, b, c


first = "boy"
second = "girl"

# 두 변수의 내용을 서로 바꾸려면?
'''
tmp = first
first = second
second =tmp

'''
second, first =first, second

print "first:",first,"second:",second
