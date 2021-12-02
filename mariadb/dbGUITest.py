import pymysql
from tkinter import *
from tkinter import messagebox

# 데이터베이스 연동 함수 선언
def insertData():
    conn = None
    cur = None

    # 데이터 베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')

    # 이것은 커서이다.
    cur = conn.cursor()


    # 회원 정보 insert 구현
    # 사용자에게 입력받은 회원 정보 초기화
    userID = edt1.get()
    name = edt2.get()
    birthYear = edt3.get()
    addr = edt4.get()

    #SQL 쿼리만들기
    sql = ""
    sql = "INSERT INTO userTBL (userID, name, birthYear, addr, mDate) VALUES " \
          "('" + userID + "', '" + name + "', " + birthYear + ", '" + addr + "', CURDATE())"

    print(sql)
    # 쿼리 실행
    try:
        cur.execute(sql)
    except:
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생했습니다.")

    else:
        # 쿼리 실행이 완료 (오류 없이)
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공", "회원정보가 등록 되었습니다.")
        # 2) 데이터 커밋(진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로 고침)
        selectData()

    # GUI에 입력한 데이터 삭제하는게 좋을 것 같다.(gui에 입력한 값을 지우는 것)
    edt1.delete(0, "end")
    edt2.delete(0, "end")
    edt3.delete(0, "end")
    edt4.delete(0, "end")

    # DB 접속 종료
    conn.close()


def selectData():
    conn = None
    cur = None

    lUserID, lName, lBirthYear, lAddr = [], [], [], []

    # 데이터 베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')

    # 이것은 커서이다.
    cur = conn.cursor()
    #데이터 초기화
    lUserID.append("회원 ID")
    lUserID.append("======")
    lName.append("회원명")
    lName.append("======")
    lBirthYear.append("출생년도")
    lBirthYear.append("======")
    lAddr.append("회원주소")
    lAddr.append("======")




    # 회원 정보 select 기능 구현
    sql = "SELECT userID, name, birthYear, addr from userTBL ORDER BY mDate DESC"
    cur.execute(sql)

    while(True) :
        row = cur.fetchone()

        if row == None:
            break
        #lUserID, lName, lBirthYear, lAddr
        lUserID.append(row[0])
        lName.append(row[1])
        lBirthYear.append(row[2])
        lAddr.append(row[3])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1. 리스트박스 초기화를 시킨다. 화면을 안지워주면 밑에 붙게 되어있다.
    # gui에서 선언한 listUserID 이것들
    listUserID.delete(0, listUserID.size() -1)
    listName.delete(0, listName.size() -1)
    listBirthYear.delete(0, listBirthYear.size() -1)
    listAddr.delete(0, listAddr.size() -1)

    # 2. select 해온 데이터 insert
    # 데이터에서 가져온 lUserID 이것들
    for item1, item2, item3, item4 in zip(lUserID, lName, lBirthYear, lAddr):
        listUserID.insert(END, item1)
        listName.insert(END, item2)
        listBirthYear.insert(END, item3)
        listAddr.insert(END, item4)


    conn.close()


# GUI 화면 구성
window = Tk()
window.geometry("800x300")
window.title("MariaDB 데이터 입력")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text="회원 ID") # 회원 결과박스
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10) # 텍스트박스이다.
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="회원명")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="출생년도")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="회원 주소")
label4.pack(side=LEFT, padx=10, pady=10)

edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

# 버튼영역
btnInsert = Button(editFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(editFrame, text="조회", command=selectData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

# 리스트 영역
listUserID = Listbox(listFrame)
listUserID.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listBirthYear = Listbox(listFrame)
listBirthYear.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()