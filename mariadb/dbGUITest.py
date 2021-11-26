import pymysql

conn = None
cur = None

# 데이터 베이스 접속
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')

# 이것은 커서이다.
cur = conn.cursor()

sql = "SELECT userID, name, birthYear, addr,"\
      "IFNULL(CONCAT(mobile1, '-', mobile2), '-') AS mobile, "\
      "IFNULL(height,0) AS height , "\
      "IFNULL(mDate,'-') AS mDate " \
      "FROM userTBL"



cur.execute(sql)
print("회원 ID    회원명    출생년도    주소      연락처     키    가입일")
print("-----------------------------------------------------------")

while(True):
    row = cur.fetchone()
    if row == None :
        break
    UserID = row[0]
    name = row[1]
    birthYear = row[2]
    addr = row[3]
    mobile = row[4]
    height = row[5]
    mDate = row[6]

    print("%5s   %5s      %d %5s  %10s %d %5s" % ( UserID, name, birthYear, addr, mobile, height, mDate))
conn.close()