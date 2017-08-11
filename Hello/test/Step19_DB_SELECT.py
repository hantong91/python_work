#-*- coding: utf-8 -*-
import mysql.connector
from errno import errorcode

config={
        "user":"root",
        "password":"maria",
        "host":"127.0.0.1",
        "database":"acorn",
        "port":3306
    }
try:
    #Maria DB 연결 객체 
    #**config => kwargs 를 dict type 으로 매칭 시키기
    conn =mysql.connector.connect(**config)
                                    # user=root, password=maria, ...이렇게 적으면 귀찮으니까 아예 위에 딕트타입으로 만든형식을 집어넣음
   
    # DB에 select, insert, update, selete 작업을 수행할 객체
    cursor=conn.cursor()
    
    #실행할 sql문 준비하기
    sql =u"SELECT NUM,NAME,ADDR FROM MEMBER ORDER BY NUM"
                                               
    # cursor 객체를 이용해서 수행한다.
    cursor.execute(sql)
    # select 된 결과 목록 얻어오기
    resultList= cursor.fetchall()  #tuple 이 들어있는 list
    print resultList
                                               
    # DB에 저장된 회원 목록 출력해보기
    for item in resultList:
        # item 은 1명의 회원 정보가 들어있는 tuple이다.
        num= item[0] #번호
        name = item[1] #이름
        addr = item[2] #주소
        
        info =u"번호:{}, 이름:{}, 주소:{}".format(num, name, addr)
        
        print info
    print u"member 테이블에 정보를 저장했습니다."
except mysql.connector.Error as err:
    # 예외가 발생했을때 수행할 작업
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print "아이디 혹은 비밀번호가 틀려요"
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print "DB 오류"
    else:        
        print "기타 오류"
    conn.rollback()
else:
    print "정상 수행 했습니다."
finally:
    #예외가 발생하던 안하던 수행이 보장되는 블럭에서 마무리 작업
    cursor.close()
    conn.close()                