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
    # db 에 select, insert, update, delete 작업을 수행할 객체
    cursor=conn.cursor()
    
    #select 할 회원의 번호범위 라고 가정하자
    num1=1
    num2=5
    
    # 실행할 select 문 구성
    sql="SELECT num,name,addr FROM member \
        WHERE num >= %s and num <= %s"
    
    # selection 인자를 tuple 에 준비한다.
    sql_arg=(num1, num2)
    
    # cursor 객체를 이용해서 수행한다.
    cursor.execute(sql, sql_arg)
    # select 된 결과 목록 얻어오기
    resultList=cursor.fetchall()   # 회원정보가 들어 있는 list  fetchall()은 select해서 결과가 1개이상 1개면 fetchone()
    for item in resultList:
        num=item[0]
        name=item[1]
        addr=item[2]
        info=u"번호:{}, 이름:{}, 주소:{}"\
            .format(num, name, addr)
        print info 
   
    
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
