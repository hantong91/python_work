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
    
    #삭제할 회원의 번호라고 가정하자
    num1=5
    sql=u"DELETE FROM member WHERE NUM=%s"
    sql_arg=(num1,)
    cursor.execute(sql,sql_arg)
    conn.commit()
    print num1, "번 회원을 삭제 했습니다."   
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