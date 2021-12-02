import pymysql
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("PythonGuides")


frame = Frame(window)
frame.pack(pady=20)

tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height=8)
tv.pack(side=LEFT)

tv.heading(1, text="1") # 열
tv.heading(2, text="2")
tv.heading(3, text="3")
tv.heading(4, text="4")
tv.heading(5, text="5")
tv.heading(6, text="6")
tv.heading(7, text="7")


sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

tv.config(yscrollcommand=sb.set)
sb.config(command=tv.yview)

def update_item():
    conn = None
    cur = None

    # 데이터 베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='stock', charset='utf8')

# 이것은 커서이다.
    cur = conn.cursor()

# 회원 정보 select 기능 구현


    sql = "SELECT * from nametbl LIMIT "
    r_set = conn.execute(sql)


    for dt in r_set:
        trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4]))


    while (True):
       row = cur.fetchall()

       if row == None:
           break

    for item1, item2, item3, item4, item5, item6, item7 in zip(lcode, lName, lprice, lsales, lprofit, lpbr, ldps):
        listcode.insert(END, item1)
        listName.insert(END, item2)
        listprice.insert(END, item3)
        listsales.insert(END, item4)
        listprofit.insert(END, item5)
        listpbr.insert(END, item6)
        listdps.insert(END, item7)

tv.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00, 1, 1, 1, 1))


style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

window.mainloop()

