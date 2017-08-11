#-*- coding: utf-8 -*-

import mysql.connector
from errno import errorcode

#DB 접속정보를 dict type으로 준비한다.

#디폴트 port 번호는 3306
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
    print conn
    
    #member 테이블에 저장할 정보
    name1 = u"뭐"
    addr1 = u"지"
    
    #실행할 sql문 준비하기
    sql =u"INSERT INTO member(name,addr) VALUES(%s,%s)"
                                                # java에서는 ? 로 했지만 파이썬은 %s
    # %s 에 바인딩할 내용을  tuple type에 담는다.
    sql_arg=(name1,addr1)
    
    # DB에 select, insert, update, delete 등의 작업을 
    # 할 객체
    cursor=conn.cursor()
    # .execute(수행할 sql문, %s 바인딩할 인자들)
    cursor.execute(sql,sql_arg)
    
    conn.commit()
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