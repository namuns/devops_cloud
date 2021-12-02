import pymysql

conn = None
cur = None

# 데이터 베이스 접속
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')

# 이것은 커서이다.
cur = conn.cursor()

# 과제 userTBL의 회원 데이터 INSERT (NULL 없이 모든 컬럼의 데이터)
# 데이터 Insert
sql = ""

# notNull 인 애들인 UserID, name, birthYear, addr 변수 선언
UserID = ""
name = ""
birthYear = ""
addr = ""
mobile1 = ""
mobile2 = ""
height = ""

while(True) :
    userID = input("사용자 ID ==> ")
    if userID == "" :
        break
    name = input("사용자 이름 ==> ")
    birthYear = input("사용자 출생년도 ==> ")
    addr = input("사용자 주소 ==> ")
    mobile1 = input("국번 ==> ")
    mobile2 = input("하이픈 없이 번호 ==> ")
    height = input("키 ==> ")

    sql = "INSERT INTO userTBL (UserID, name, birthYear, addr, mobile1, mobile2, height, mDate) VALUES"\
          "('" + userID + "', '" + name + "', " + birthYear + ", '" + addr + "', '" + mobile1 + "', '" + mobile2 + "', '" + height + "', CURDATE())"

# 인서트문에 (UserID, name, birthYear, addr, mobile1, mobile2, height, mDate)는 제외 가능.
# INT 라서 작은따옴표 안쓰는 birthYear 텍스트는 아니니까, 플러스는 텍스트를 연결해주는 연결자를 안해주면 하나하나 하드코딩해야한다.
# 작은따옴표를 하나 더 넣어주는 이유는 쿼리문에서 str이라는거 알려주기위해서.
    cur.execute(sql)

conn.commit()
conn.close()
