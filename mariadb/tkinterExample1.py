from tkinter import *

# 문자를 표현할 수 있는 라벨 사용
window = Tk()
window.title("라벨 연습")
window.geometry("400x180") #넓이 x 높이

label1 = Label(window, text="This is MariaDB를")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="magenta")
label3 = Label(window, text="공부 중입니다.", font=("궁서체", 30), bg="magenta", width=20, height=5, anchor=CENTER)
    # 레이블이 올라갈 윈도우, 텍스트=출력될 글, 폰트는 폰트, fg는 글자색, bg는 배경색, anchor는 글자의 위치

#실제 위젯 적용은 밑에있는 애들이다.
label1.pack()
label2.pack()
label3.pack()

window.mainloop()



