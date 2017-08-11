#-*- coding: utf-8 -*-

import mysql.connector
from errno import errorcode

#DB 접속정보를 dict type 으로 준비한다.

config={
        "user":"root",
        "password":"maria",
        "host":"127.0.0.1",
        "database":"acorn",
        "port":3306
    }
try:
    #Maria DB 연결 객체
    # **config   => kwargs 를 dict type 으로 매칭 시키기 
    conn=mysql.connector.connect(**config)
    cursor=conn.cursor()
    
    #수정할 회원의 정보라고 가정
    num1=1
    name1=u"아무게"
    addr1=u"어디게"
    #실행할 sql 문
    sql=u"UPDATE member SET NAME=%s,ADDR=%s WHERE num=%s"
    # update 문에 바인딩할 인자들
    sql_arg=(name1, addr1, num1)
    # update 문 수행
    cursor.execute(sql, sql_arg)
    conn.commit() # DB 에 실제 반영
    print num1, u" 번 회원의 정보를 수정 했습니다."
   
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
    # 예외가 발생하던 안하던 수행이 보장되는 블럭에서 마무리 작업
    cursor.close()
    conn.close()