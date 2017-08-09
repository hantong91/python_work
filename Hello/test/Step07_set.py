#-*- coding: utf-8 -*-
'''
 
 
  - set type'
  
   1. 순서가 없다
   2. 중복을 허용하지 않는다.
   3. 집합(묶음) 이라고 생각하면 된다.
   
   
'''



# set type 데이터 만들기

set1 = {10,20,30,40,50}

print set1
print "len(set1)", len(set1)


# set type 에 데이터 추가하기
set1.add(60)
set1.add(70)
set1.add(70)
set1.add(70)
set1.add(10)

print "set1:", set1

# 새로운 set type 데이터블 만들고
set2={60,70,80,90,100}

# 두 set 간의 합집합
unionResult = set1.union(set2)

print "set union set2 : ", unionResult

# 두 set 간의 교집합

intersectionResult = set1.intersection(set2)

print "set1 intersection set2:", intersectionResult

# 두 set 간의 차입합

minusResult = set1 -set2
print "set1 - set2 :", minusResult



set3={"kim","lee"}
list1 = ["park","cho","lee"]
tuple1 = ("one", "two")

# set 에 list type 이나 tuple type 에 있는 원소 병합 시키기
set3.update(list1)
print "list1 병합후 set3:", set3

set3.update(tuple1)
print "tuple1 병합후 set3:", set3

#값 삭제 
set3.discard("park")
print "set3 에서 park discard 이후:",set3
#삭제할 값이 존재하지 않으면...
set3.discard("김구라") # 무시한다. 

#값 삭제 remove() 이용 
#삭제할 값이 존재하지 않으면 ...
#set3.remove("해골") # 예외 발생!

#값 모두 삭제
set3.clear()
print "set3 clear() 이후 : ",set3

# 반복문 돌면서 set1 에 저장된 모든 내용 불러와서 작업
for item in set1:
    print item
    
# list 에 저장된 데이터에서 중복을 제거 하고 싶다라면 ...    
list3 = [10,20,30,10,10,30,40,50,50]
# set 를 이용한다.
set4 = set(list3)
print "set4 : ",set4
# 중복 제거후 다시 list type 으로 얻어낸다.
list4 = list(set4)
print "list4 : ",list4