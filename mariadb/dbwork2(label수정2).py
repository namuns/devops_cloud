import pymysql
import tkinter
import os
from tkinter import *
from tkinter import messagebox


# 데이터베이스 연동 함수 선언
def insertData():
    conn = None
    cur = None

    # 데이터 베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='stock', charset='utf8')

    # 이것은 커서이다.
    cur = conn.cursor()


    # 회원 정보 insert 구현
    # 사용자에게 입력받은 회원 정보 초기화
    code = edt1.get()
    name = edt2.get()
    price = edt3.get()
    sales = edt4.get()
    profit = edt5.get()
    pbr = edt6.get()
    dps = edt7.get()

    #SQL 쿼리만들기
    sql = ""
    sql = "INSERT INTO stockTBL (code, name, price, sales, profit, pbr, dps) VALUES " \
          "('" + code + "', '" + name + "', " + price + ", '" + sales + "', '" + profit + "',  '" + pbr + "', '" + dps + "')"

    print(sql)
    # 쿼리 실행
    try:
        cur.execute(sql)
    except:
        messagebox.showerror("입력오류", "올바른 값을 입력해주세요.")

    else:
        # 쿼리 실행이 완료 (오류 없이)
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공", "주식 정보가 등록 되었습니다.")
        # 2) 데이터 커밋(진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로 고침)
        selectData()

    # GUI에 입력한 데이터 삭제하는게 좋을 것 같다.(gui에 입력한 값을 지우는 것)
    edt1.delete(0, "end")
    edt2.delete(0, "end")
    edt3.delete(0, "end")
    edt4.delete(0, "end")
    edt5.delete(0, "end")
    edt6.delete(0, "end")
    edt7.delete(0, "end")

#def deleteData():


# 프레임 이동( 메인화면으로 돌아가기)
def backFrame():
    editFrame.pack()
    listFrame.pack_forget()

# 조회
def checkList():
    conn = None
    cur = None

    code = edt1.get()

    editFrame.pack_forget()
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    lcode, lName, lprice, lsales, lprofit, lpbr, ldps = [], [], [], [], [], [], []

    # 데이터 베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='stock', charset='utf8')

    # 이것은 커서이다.
    cur = conn.cursor()
    # 데이터 초기화
    lcode.append("티거")
    lcode.append("======")
    lName.append("회사이름")
    lName.append("======")
    lprice.append("주가")
    lprice.append("======")
    lsales.append("매출액")
    lsales.append("======")
    lprofit.append("영업이익")
    lprofit.append("======")
    lpbr.append("PBR")
    lpbr.append("======")
    ldps.append("DPS")
    ldps.append("======")


    # 회원 정보 select 기능 구현
    sql = "SELECT code, name, price, sales, profit, pbr, dps from stockTBL ORDER BY code ASC"
    cur.execute(sql)

    while(True) :
        row = cur.fetchone()

        if row == None:
            break

        lcode.append(row[0])
        lName.append(row[1])
        lprice.append(row[2])
        lsales.append(row[3])
        lprofit.append(row[4])
        lpbr.append(row[5])
        ldps.append(row[6])
    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1. 리스트박스 초기화를 시킨다. 화면을 안지워주면 밑에 붙게 되어있다.
    # gui에서 선언한 listUserID 이것들
    listcode.delete(0, listcode.size() -1)
    listName.delete(0, listName.size() -1)
    listprice.delete(0, listprice.size() -1)
    listsales.delete(0, listsales.size() -1)
    listprofit.delete(0, listprofit.size() -1)
    listpbr.delete(0, listpbr.size() -1)
    listdps.delete(0, listdps.size() -1)

    # 2. select 해온 데이터 insert
    # 데이터에서 가져온 lUserID 이것들
    for item1, item2, item3, item4, item5, item6, item7 in zip(lcode, lName, lprice, lsales, lprofit, lpbr, ldps):
        listcode.insert(END, item1)
        listName.insert(END, item2)
        listprice.insert(END, item3)
        listsales.insert(END, item4)
        listprofit.insert(END, item5)
        listpbr.insert(END, item6)
        listdps.insert(END, item7)


    conn.close()

# 검색
def selectData():
    conn = None
    cur = None

    code = edt8.get()

    editFrame.pack_forget()
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)


    lcode, lName, lprice, lsales, lprofit, lpbr, ldps = [], [], [], [], [], [], []

    # 데이터 베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='stock', charset='utf8')

    # 이것은 커서이다.
    cur = conn.cursor()
    #데이터 초기화
    lcode.append("티거")
    lcode.append("======")
    lName.append("회사이름")
    lName.append("======")
    lprice.append("주가")
    lprice.append("======")
    lsales.append("매출액")
    lsales.append("======")
    lprofit.append("영업이익")
    lprofit.append("======")
    lpbr.append("PBR")
    lpbr.append("======")
    ldps.append("DPS")
    ldps.append("======")


    # 회원 정보 select 기능 구현
    sql = "SELECT code, name, price, sales, profit, pbr, dps from stockTBL WHERE code ='"+code+"' ORDER BY code DESC"
    cur.execute(sql)

    while(True) :
        row = cur.fetchone()

        if row == None:
            break
        # lcode, lName, lprice, lsales, lprofit, lpbr, ldps
        lcode.append(row[0])
        lName.append(row[1])
        lprice.append(row[2])
        lsales.append(row[3])
        lprofit.append(row[4])
        lpbr.append(row[5])
        ldps.append(row[6])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1. 리스트박스 초기화를 시킨다. 화면을 안지워주면 밑에 붙게 되어있다.
    # gui에서 선언한 listUserID 이것들
    listcode.delete(0, listcode.size() -1)
    listName.delete(0, listName.size() -1)
    listprice.delete(0, listprice.size() -1)
    listsales.delete(0, listsales.size() -1)
    listprofit.delete(0, listprofit.size() -1)
    listpbr.delete(0, listpbr.size() -1)
    listdps.delete(0, listdps.size() -1)

    # 2. select 해온 데이터 insert
    # 데이터에서 가져온 lUserID 이것들
    for item1, item2, item3, item4, item5, item6, item7 in zip(lcode, lName, lprice, lsales, lprofit, lpbr, ldps):
        listcode.insert(END, item1)
        listName.insert(END, item2)
        listprice.insert(END, item3)
        listsales.insert(END, item4)
        listprofit.insert(END, item5)
        listpbr.insert(END, item6)
        listdps.insert(END, item7)


    conn.close()

# 계산
def calculate1():
    conn = None
    cur = None

    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    lcode = []
    # 데이터 베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='stock', charset='utf8')
    # 이것은 커서이다.
    cur = conn.cursor()
    # 데이터 초기화
    lcode.append("BPS 값")
    lcode.append("======")

    # 회원 정보 select 기능 구현
    sql = "SELECT (pbr/price*100) AS 'BPS 구하기' from stocktbl ORDER BY code DESC"

    cur.execute(sql)
    while True:
        row = cur.fetchone()

        if row == None:
            break
        #
        lcode.append(row[0])

    listcode.delete(0, listcode.size() - 1)

    for item1, in zip(lcode):
        listcode.insert(END, item1)

    conn.close()



# GUI 화면 구성
window = tkinter.Tk()
window.geometry("1550x800")
window.title("영웅문")


image=tkinter.PhotoImage(file="unnamed.png")

label=tkinter.Label(window, image=image)
label.pack()

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack()
listFrame.pack_forget()


label1 = Label(editFrame, text="티거") # 회원 결과박스
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10) # 텍스트박스이다.
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="회사이름")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="주가")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="매출액")
label4.pack(side=LEFT, padx=10, pady=10)

edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

label5 = Label(editFrame, text="영업이익")
label5.pack(side=LEFT, padx=10, pady=10)

edt5 = Entry(editFrame, width=10)
edt5.pack(side=LEFT, padx=10, pady=10)


label6 = Label(editFrame, text="PBR")
label6.pack(side=LEFT, padx=10, pady=10)

edt6 = Entry(editFrame, width=10)
edt6.pack(side=LEFT, padx=10, pady=10)


label7 = Label(editFrame, text="DPS")
label7.pack(side=LEFT, padx=10, pady=10)

edt7 = Entry(editFrame, width=10)
edt7.pack(side=LEFT, padx=10, pady=10)


label8 = Label(editFrame, text="*단위:백만달러(USD)")
label8.pack(side=LEFT, padx=10, pady=10)

edt8 = Entry(editFrame, width=10)
edt8.pack(side=RIGHT, padx=10, pady=10)

# 버튼영역
btnInsert = Button(editFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(editFrame, text="조회", command=checkList)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(editFrame, text="검색", command=selectData)
btnInsert.pack(side=RIGHT, padx=10, pady=10)

# 리스트 영역
listcode = Listbox(listFrame)
listcode.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listprice = Listbox(listFrame)
listprice.pack(side=LEFT, fill=BOTH, expand=1)

listsales = Listbox(listFrame)
listsales.pack(side=LEFT, fill=BOTH, expand=1)

listprofit = Listbox(listFrame)
listprofit.pack(side=LEFT, fill=BOTH, expand=1)

listpbr = Listbox(listFrame)
listpbr.pack(side=LEFT, fill=BOTH, expand=1)

listdps = Listbox(listFrame)
listdps.pack(side=LEFT, fill=BOTH, expand=1)

btnBack = Button(listFrame, text="돌아가기", command=backFrame)
btnBack.pack(side=LEFT, padx=10, pady=10)

btnBack = Button(listFrame, text="BPS 계산", command=calculate1)
btnBack.pack(side=LEFT, padx=10, pady=10)

btnBack = Button(listFrame, text="적정주가 계산", command=calculate1)
btnBack.pack(side=LEFT, padx=10, pady=10)


#

window.mainloop()

